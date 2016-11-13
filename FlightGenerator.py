#!/usr/bin/python
import urllib2
import time

import DateData
import Plotter
from Config import IS_DEBUG_MODE_SET, DUMMY_DEPARTURE_AND_ARRIVAL_DATE, URL_REQUEST, DAYS_SHIFTER, PERIOD, SLEEP_TIME, PLOT_WIDTH, PLOT_HEIGHT, PLOT_PPI
from GlobalFunctions import convertStringToInt


class FlightGenerator:
  
  def __init__(self):
    self.dictionaryContainerForPlot = dict()
    self.dateDataInstance = DateData.DateData()
    
  def setDepartureAndArrivalDateInURLRequest(self, shiftedTime, urlRequest):
    shiftedTimeAsString = self.dateDataInstance.getFormatedDateForURLRequestAsString(shiftedTime)
    #print 'shiftedTimeAsString= ', shiftedTimeAsString
    mountedURLRequest = urlRequest.replace(DUMMY_DEPARTURE_AND_ARRIVAL_DATE, shiftedTimeAsString)	#urlRequest.replace(DUMMY_DEPARTURE_AND_ARRIVAL_DATE, shiftedTimeAsString, 2)
    return mountedURLRequest
  
  def cutSubstring(self, startSign, stopSign, content):
    startIndex = content.find(startSign)
    stopIndex = content.find(stopSign)
    felledSubstring = content[startIndex + 1 : stopIndex]
    return felledSubstring
  
  def getSingleFare(self, startIndex, substringLen, htmlContent):
    htmlOffset = 18	#Total: <span class="bp">528 zl</span><br/>
    htmlSubstringWithFareStartIndex = startIndex + substringLen + htmlOffset
    htmlOffset = 10	#528 zl</s	get first 10 signs and cut
    htmlSubstringWithFareStopIndex = htmlSubstringWithFareStartIndex + htmlOffset
    htmlSubstringContent = htmlContent[htmlSubstringWithFareStartIndex : htmlSubstringWithFareStopIndex]
    #print 'htmlSubstringContent= ', htmlSubstringContent
    singleFare = self.cutSubstring('>', ' ', htmlSubstringContent)
    #print 'singleFare= ', singleFare
    return singleFare
  
  def getTotalFaresFromHtmlContent(self, htmlContent):
    wantedStringToFindFare = 'Total:'
    faresListContainer = []
    wantedSubstringLen = len(wantedStringToFindFare)
    htmlContentLen = len(htmlContent)
    htmlContentRange = range(0, htmlContentLen)

    for htmlContentRangeIterator in htmlContentRange:
      wantedSubstringLenIndex = htmlContentRangeIterator + wantedSubstringLen
      
      if htmlContent[htmlContentRangeIterator : wantedSubstringLenIndex] == wantedStringToFindFare:
        singleFare = self.getSingleFare(htmlContentRangeIterator, wantedSubstringLen, htmlContent)
        singleFare = convertStringToInt(singleFare)
        faresListContainer.append(singleFare)
        htmlContentRangeIterator = htmlContentRangeIterator + 1
    return faresListContainer
  
  def getLowestFare(self, faresListContainer):
    if faresListContainer:
      #print 'min(faresListContainer)= ', min(faresListContainer)
      return min(faresListContainer)

  def getHighestFare(self, faresListContainer):
    if faresListContainer:
      #print 'max(faresListContainer) =', max(faresListContainer)
      return max(faresListContainer)

  def getHtmlContent(self, URLrequest):
    requestURL = urllib2.Request(URLrequest)

    try:
      responseURL = urllib2.urlopen(requestURL)
    except URLError as errorUrl:
      print errorUrl.reason
      
    htmlContent = responseURL.read()
    return htmlContent

  def handleHtmlContent(self, currentDate, daysShifter):
    shiftedTime = self.dateDataInstance.getTimeShifted(currentDate, daysShifter)
    #print 'shiftedTime=', shiftedTime
    mountedURLRequest = self.setDepartureAndArrivalDateInURLRequest(shiftedTime, URL_REQUEST)
    #print 'mountedURLRequest:\n', mountedURLRequest, "\n"
    htmlContent = self.getHtmlContent(mountedURLRequest)
    faresListContainer = self.getTotalFaresFromHtmlContent(htmlContent)
    self.prepareDictionaryContainerWithLowestFaresForPlot(faresListContainer, shiftedTime)

  def prepareDictionaryContainerWithLowestFaresForPlot(self, dataListContainer, shiftedTime):
    lowestPrice = self.getLowestFare(dataListContainer)
    
    if IS_DEBUG_MODE_SET:
      print 'dataListContainer= ', dataListContainer
    self.dictionaryContainerForPlot[shiftedTime] = lowestPrice

  def calculateFlight(self):
    currentDate = self.dateDataInstance.getCurrentDate()
    daysShifterTemporary = DAYS_SHIFTER
    
    while daysShifterTemporary != PERIOD:
      self.handleHtmlContent(currentDate, daysShifterTemporary)
      daysShifterTemporary = daysShifterTemporary + 1
      time.sleep(SLEEP_TIME)
      
  def generatePlot(self):
    if self.dictionaryContainerForPlot:
      plotterInstance = Plotter.Plotter(PLOT_WIDTH, PLOT_HEIGHT, PLOT_PPI, self.dictionaryContainerForPlot)
      plotterInstance.generatePlot()

  def generateFlightsFaresWithPlot(self):
    self.calculateFlight()
    self.generatePlot()
    