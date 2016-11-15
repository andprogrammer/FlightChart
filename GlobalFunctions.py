#!/usr/bin/python
import os

from Config import IS_DEBUG_MODE_SET


def convertStringToInt(content):
  if content:
    return int(content)
  return 0	#TODO handle this case

def createDirectoryIfNotExist(directoryName):
  if not os.path.exists(directoryName):
    os.makedirs(directoryName)

def convertDate(date):
  return date.strftime('%Y-%m-%d')
  
def PRINT_DEBUG(argument, value):
  if IS_DEBUG_MODE_SET:
    print argument + "=", value
  