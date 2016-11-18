#!/usr/bin/python
import urllib2
import time

import DateData
import Plotter
from Config import (
  DUMMY_DEPARTURE_AND_ARRIVAL_DATE,
  URL_REQUEST, 
  DAYS_SHIFTER, 
  PERIOD, 
  SLEEP_TIME, 
  PLOT_WIDTH, 
  PLOT_HEIGHT, 
  PLOT_PPI
)
from GlobalFunctions import convertStringToInt, convertDate, PRINT_DEBUG#, printConfigSettings


class FlightGenerator:
  
  def __init__(self):
    self.dictionaryForPlot = dict()
    self.dateDataInstance = DateData.DateData()
    self.lowestFare = 99999   #sys.maxsize  #import sys  #try: except ImportError:
    self.lowestFareDate = None
    
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
    faresList = []
    wantedSubstringLen = len(wantedStringToFindFare)
    htmlContentLen = len(htmlContent)
    htmlContentRange = range(0, htmlContentLen)

    for htmlContentRangeIterator in htmlContentRange:
      wantedSubstringLenIndex = htmlContentRangeIterator + wantedSubstringLen
      
      if htmlContent[htmlContentRangeIterator : wantedSubstringLenIndex] == wantedStringToFindFare:
        singleFare = self.getSingleFare(htmlContentRangeIterator, wantedSubstringLen, htmlContent)
        
        if singleFare:
          singleFare = convertStringToInt(singleFare)
          faresList.append(singleFare)
          htmlContentRangeIterator = htmlContentRangeIterator + 1
    return faresList
  
  def getLowestFare(self, faresList):
    if faresList:
      #print 'min(faresList)= ', min(faresList)
      return min(faresList)

  def getHighestFare(self, faresList):
    if faresList:
      #print 'max(faresList) =', max(faresList)
      return max(faresList)

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
    
    if mountedURLRequest:
      htmlContent = self.getHtmlContent(mountedURLRequest)
      
      if htmlContent:
        faresList = self.getTotalFaresFromHtmlContent(htmlContent)
        
        if faresList:
          self.prepareDictionaryWithLowestFaresForPlot(faresList, shiftedTime)

  def setLowestFare(self, fare, date):
    if fare < self.lowestFare:
      self.lowestFare = fare
      self.lowestFareDate = convertDate(date)

  def prepareDictionaryWithLowestFaresForPlot(self, dataList, shiftedDate):
    lowestFare = self.getLowestFare(dataList)
    
    if lowestFare:
      self.setLowestFare(lowestFare, shiftedDate)
      
      PRINT_DEBUG("dataList", dataList)
      self.dictionaryForPlot[shiftedDate] = lowestFare

  def calculateFlight(self):
    currentDate = self.dateDataInstance.getCurrentDate()
    daysShifterTemporary = DAYS_SHIFTER
    
    while daysShifterTemporary != PERIOD:
      self.handleHtmlContent(currentDate, daysShifterTemporary)
      daysShifterTemporary = daysShifterTemporary + 1
      time.sleep(SLEEP_TIME)
      
  def generatePlot(self):
    if self.dictionaryForPlot:
      plotterInstance = Plotter.Plotter(PLOT_WIDTH, PLOT_HEIGHT, PLOT_PPI, self.dictionaryForPlot)
      plotterInstance.generatePlot()

  def generateFlightsFaresWithPlot(self):
    #printConfigSettings()
    self.calculateFlight()
    self.generatePlot()
    PRINT_DEBUG("lowestFare", self.lowestFare)
    PRINT_DEBUG("lowestFareDate", self.lowestFareDate)
    