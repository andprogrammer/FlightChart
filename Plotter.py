#!/usr/bin/python
import matplotlib.pyplot as matplot
from pprint import pprint

import DateData
from Config import DESTINATION_DIRECTORY_WITH_PLOTS, DESTINATION_DIRECTORY_WITH_FARES, IS_DEBUG_MODE_SET, SAVE_FLIGHTS_FARES_TO_FILE
from GlobalFunctions import createDirectoryIfNotExist


class Plotter:
  
  def __init__(self, width, height, ppi, dataDictionary, destinationDirectory = DESTINATION_DIRECTORY_WITH_PLOTS):
    self.width = width
    self.height = height
    self.ppi = ppi
    self.dataDictionary = dataDictionary
    self.destinationDirectory = destinationDirectory
    self.dateDataInstance = DateData.DateData()
    
  def saveListToFile(self, orderedList):
    
    destinationDirectory = DESTINATION_DIRECTORY_WITH_FARES
    createDirectoryIfNotExist(destinationDirectory)
    currentDate = DateData.DateData().getCurrentDate()
    faresFilename = destinationDirectory + '/' + currentDate.strftime('%Y-%m-%d') + '.txt'
    
    fileDescryptor = open(faresFilename, "w")
    for orderedListIterator in orderedList:	#iterate through list
      isDateSet = False
      for tupleIterator in orderedListIterator:	#iterate through tuple
	#print tupleIterator
	if not isDateSet:
	  convertedDate = tupleIterator.strftime('%d/%m/%Y')
	  fileDescryptor.write("Date: |%s| " % convertedDate)
	  isDateSet = True
	else:
	  fileDescryptor.write("Fare: |%s|\n" % tupleIterator)
	  isDateSet = False
    fileDescryptor.close()
    
  def prepareData(self):
    orderedListData = sorted(self.dataDictionary.items())	#sort ascending by date (key)
    
    if IS_DEBUG_MODE_SET:
      pprint(orderedListData)
    if SAVE_FLIGHTS_FARES_TO_FILE:
      self.saveListToFile(orderedListData)

    return orderedListData
    
  def preparePlot(self, dataDictionary):
    matplot.figure(figsize = (self.width / self.ppi, self.height / self.ppi), dpi = self.ppi)
    xAxis, yAxis = zip(*dataDictionary)
    matplot.plot(xAxis, yAxis)
    
  def savePlot(self):
    createDirectoryIfNotExist(self.destinationDirectory)
    currentDate = self.dateDataInstance.getCurrentDate()
    plotFilename = self.destinationDirectory + '/' + currentDate.strftime('%Y-%m-%d') + '.png'
    matplot.savefig(plotFilename, dpi=self.ppi, bbox_inches='tight')
    
  def generatePlot(self):
    orderedListData = self.prepareData()
    self.preparePlot(orderedListData)
    self.savePlot()
    