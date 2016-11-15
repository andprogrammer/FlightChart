#!/usr/bin/python
import matplotlib.pyplot as matplot
from pprint import pprint

import DateData
from Config import (
  DESTINATION_DIRECTORY_WITH_PLOTS, 
  DESTINATION_DIRECTORY_WITH_FARES, 
  IS_DEBUG_MODE_SET, 
  SAVE_FLIGHTS_FARES_TO_FILE, 
  IS_ONE_WAY, 
  SOURCE_AIRPORT, 
  DESTINATION_AIRPORT, 
  NUMBER_OF_ADULTS, 
  NUMBER_OF_CHILDREN, 
  NUMBER_OF_INFANTS, 
  MAX_CHANGES, 
  CURRENCY, 
  PERIOD,
)
from GlobalFunctions import createDirectoryIfNotExist, convertDate, PRINT_DEBUG


class Plotter:
  
  def __init__(self, width, height, ppi, dataDictionary, destinationDirectory = DESTINATION_DIRECTORY_WITH_PLOTS):
    self.width = width
    self.height = height
    self.ppi = ppi
    self.dataDictionary = dataDictionary
    self.destinationDirectory = destinationDirectory
    self.dateDataInstance = DateData.DateData()
    self.startingDate = ""
    self.endDate = ""
    
  def writeConfigSettingsToFile(self, fileDescryptor):
    fileDescryptor.write("---------------Config settings---------------\n")
    fileDescryptor.write("Flight type [oneway | return]: |%s|\n" % IS_ONE_WAY)
    fileDescryptor.write("Source airport: |%s|\n" % SOURCE_AIRPORT)
    fileDescryptor.write("Destination airport: |%s|\n" % DESTINATION_AIRPORT)
    fileDescryptor.write("Number of adults: |%s|\n" % NUMBER_OF_ADULTS)
    fileDescryptor.write("Number of children: |%s|\n" % NUMBER_OF_CHILDREN)
    fileDescryptor.write("Number of infants: |%s|\n" % NUMBER_OF_INFANTS)
    fileDescryptor.write("Max changes: |%s|\n" % MAX_CHANGES)
    fileDescryptor.write("Currency: |%s|\n" % CURRENCY)
    fileDescryptor.write("Period [days]: |%s|\n" % (PERIOD - 1))   #(PERIOD - 1) days
    fileDescryptor.write("---------------------------------------------\n")
    
  def saveListToFile(self, orderedList):
    destinationDirectory = DESTINATION_DIRECTORY_WITH_FARES
    createDirectoryIfNotExist(destinationDirectory)
    currentDate = DateData.DateData().getCurrentDate()
    convertedCurrentDate = convertDate(currentDate)
    faresFilename = destinationDirectory + '/' + convertedCurrentDate + '.txt'
    
    fileDescryptor = open(faresFilename, "w")
    self.writeConfigSettingsToFile(fileDescryptor)
    
    for orderedListIterator in orderedList:  #iterate through list
      isDateSet = False
      for tupleIterator in orderedListIterator:  #iterate through tuple
        #print tupleIterator
        if not isDateSet:
          convertedDate = tupleIterator.strftime('%d/%m/%Y')
          fileDescryptor.write("Date: |%s| " % convertedDate)
          isDateSet = True
        else:
          fileDescryptor.write("Fare: |%s|\n" % tupleIterator)
          isDateSet = False
    fileDescryptor.close()
    
  def setDates(self, orderedList):
    #[(datetime.datetime(2016, 11, 16, 11, 30, 48, 948296), 629),
    # (datetime.datetime(2016, 11, 17, 11, 30, 48, 948296), 369)]
    if orderedList:
      firstElementFromTheOrderedList = orderedList[0]
      lastElementFromTheOrderedList = orderedList[-1]
      dateFromFirstElementOfTule = firstElementFromTheOrderedList[0]
      dateFromLastElementOfTule = lastElementFromTheOrderedList[0]
      self.startingDate = convertDate(dateFromFirstElementOfTule)
      self.endDate = convertDate(dateFromLastElementOfTule)
      
      PRINT_DEBUG("startingDate", self.startingDate)
      PRINT_DEBUG("endDate", self.endDate)
    
  def getPreparedData(self):
    orderedListData = sorted(self.dataDictionary.items())	#sort ascending by date (key)
    
    if IS_DEBUG_MODE_SET:
      pprint(orderedListData)
    if SAVE_FLIGHTS_FARES_TO_FILE:
      self.saveListToFile(orderedListData)
      
    self.setDates(orderedListData)
    return orderedListData
    
  def setPlotTitle(self):
    plotTitle = "\nFlightChart [" + SOURCE_AIRPORT + " - " + DESTINATION_AIRPORT + "] [" + IS_ONE_WAY + "]\n"
    matplot.title(plotTitle, fontsize=26, color='blue')
    
  def setYLabelPlotTitle(self):
    yLabelTitle = '\nFares [' + CURRENCY + ']\n'
    matplot.ylabel(yLabelTitle, fontsize=20, color='red')
    
  def setXLabelPlotTitle(self):
    xLabelPlotTitle = "\nDates [" + self.startingDate + " - " + self.endDate + "]\n"
    matplot.xlabel(xLabelPlotTitle, fontsize=20, color='green')
    
  def preparePlot(self, orderedList):
    matplot.figure(figsize = (self.width / self.ppi, self.height / self.ppi))
    self.setPlotTitle()
    self.setYLabelPlotTitle()
    self.setXLabelPlotTitle()
    matplot.grid(True)
    xAxis, yAxis = zip(*orderedList)
    matplot.plot(xAxis, yAxis)  #matplot.plot(xAxis, yAxis, 'r^')  generate red triangle
    
  def savePlot(self):
    createDirectoryIfNotExist(self.destinationDirectory)
    currentDate = self.dateDataInstance.getCurrentDate()
    
    if currentDate:
      plotFilename = self.destinationDirectory + '/' + currentDate.strftime('%Y-%m-%d') + '.png'
      matplot.savefig(plotFilename, dpi=self.ppi, bbox_inches='tight')
    
  def generatePlot(self):
    orderedListData = self.getPreparedData()
    if orderedListData:
      self.preparePlot(orderedListData)
      self.savePlot()
    else:
      print "EMPTY DATA. UNABLE TO CREATE PLOT!"
    