#!/usr/bin/python
import os

from Config import (
  IS_DEBUG_MODE_SET,
  SAVE_FLIGHTS_FARES_TO_FILE,
  DESTINATION_DIRECTORY_WITH_PLOTS,
  DESTINATION_DIRECTORY_WITH_FARES,
  DUMMY_DEPARTURE_AND_ARRIVAL_DATE,
  IS_ONE_WAY,
  SOURCE_AIRPORT,
  DESTINATION_AIRPORT,
  NUMBER_OF_ADULTS,
  NUMBER_OF_CHILDREN,
  NUMBER_OF_INFANTS,
  MAX_CHANGES,
  CURRENCY,
  URL_REQUEST,
  DAYS_SHIFTER,
  PERIOD,
  SLEEP_TIME,
  PLOT_WIDTH,
  PLOT_HEIGHT,
  PLOT_PPI,
)


def convertStringToInt(content):
  if content:
    return int(content)
  return 0	#TODO handle this case

def createDirectoryIfNotExist(directoryName):
  if not os.path.exists(directoryName):
    os.makedirs(directoryName)

def convertDate(date):      #convert to string
  return date.strftime('%Y-%m-%d')
  
def PRINT_DEBUG(argument, value):
  if IS_DEBUG_MODE_SET:
    print argument + "=", value
  
def printConfigSettings():
  #General settings
  print "IS_DEBUG_MODE_SET=", IS_DEBUG_MODE_SET
  print "SAVE_FLIGHTS_FARES_TO_FILE=", SAVE_FLIGHTS_FARES_TO_FILE
  print "DESTINATION_DIRECTORY_WITH_PLOTS=", DESTINATION_DIRECTORY_WITH_PLOTS
  print "DESTINATION_DIRECTORY_WITH_FARES=", DESTINATION_DIRECTORY_WITH_FARES
  
  #Flights settings
  print "DUMMY_DEPARTURE_AND_ARRIVAL_DATE=", DUMMY_DEPARTURE_AND_ARRIVAL_DATE
  
  print "IS_ONE_WAY=", IS_ONE_WAY
  print "SOURCE_AIRPORT=", SOURCE_AIRPORT
  print "DESTINATION_AIRPORT=", DESTINATION_AIRPORT
  print "NUMBER_OF_ADULTS=", NUMBER_OF_ADULTS
  print "NUMBER_OF_CHILDREN=", NUMBER_OF_CHILDREN
  print "NUMBER_OF_INFANTS=", NUMBER_OF_INFANTS
  print "MAX_CHANGES=", MAX_CHANGES
  print "CURRENCY=", CURRENCY
  print "URL_REQUEST=", URL_REQUEST
  
  #Plot settings
  print "DAYS_SHIFTER=", DAYS_SHIFTER
  print "PERIOD=", PERIOD
  print "SLEEP_TIME=", SLEEP_TIME
  print "PLOT_WIDTH=", PLOT_WIDTH
  print "PLOT_HEIGHT=", PLOT_HEIGHT
  print "PLOT_PPI=", PLOT_PPI
