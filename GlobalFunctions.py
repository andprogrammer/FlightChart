#!/usr/bin/python
import os

import DateData


def convertStringToInt(content):
  if content:
    return int(content)
  return 0	#TODO handle this case

def createDirectoryIfNotExist(directoryName):
  if not os.path.exists(directoryName):
    os.makedirs(directoryName)
