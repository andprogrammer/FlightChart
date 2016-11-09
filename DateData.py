#!/usr/bin/python
import datetime
from datetime import timedelta


class DateData:
  
  def __init__(self):
    self.currentDate = datetime.datetime.now()
    self.year = self.currentDate.year
    self.month = self.currentDate.month
    self.day = self.currentDate.day
    self.hour = self.currentDate.hour
    self.minute = self.currentDate.minute
    self.second = self.currentDate.second
    self.microsecond = self.currentDate.microsecond
  
  def updateDateData(self):
    self.currentDate = datetime.datetime.now()
    self.year = self.currentDate.year
    self.month = self.currentDate.month
    self.day = self.currentDate.day
    self.hour = self.currentDate.hour
    self.minute = self.currentDate.minute
    self.second = self.currentDate.second
    self.microsecond = self.currentDate.microsecond    
  
  def getCurrentDate(self):
    return datetime.datetime.now()
  
  def getTimeShifted(self, date, daysToShift, arithmeticSign = '+'):
    timeShifted = datetime.datetime.now()
    switcher = {
      '+' : date + timedelta(days = daysToShift),
      '-' : date - timedelta(days = daysToShift),
    }
    return switcher.get(arithmeticSign, timeShifted)
  
  def getTimeShiftedFromToday(self, daysToShift, arithmeticSign = '+'):
    timeShifted = datetime.datetime.now()
    switcher = {
      '+' : timeShifted + timedelta(days = daysToShift),
      '-' : timeShifted - timedelta(days = daysToShift),
    }
    return switcher.get(arithmeticSign, timeShifted)
  
  def getFormatedYearAsString(self, date):
    return str(date.year)
  
  def getFormatedMonthAsString(self, date):
    month = date.month
    if month > 0 and month < 10:
      month = str(month)
      month = "0" + month
    else:
      month = str(month)
    return month
  
  def getFormatedDayAsString(self, date):
    day = date.day
    if day > 0 and day < 10:
      day = str(day)
      day = "0" + day
    else:
      day = str(day)
    return day
  
  def getFormatedDateForURLRequestAsString(self, date):
    year = self.getFormatedYearAsString(date)
    month = self.getFormatedMonthAsString(date)
    day = self.getFormatedDayAsString(date)
    
    formatedDateForURLRequestAsString = year + "-" + month + "-" + day
    #print 'formatedDateForURLRequestAsString= ', formatedDateForURLRequestAsString
    return formatedDateForURLRequestAsString
  
  def getYearFromDate(self, date):	#2016-11-01
    return date[:4]
  
  def getMonthFromDate(self, date):	#2016-11-01
    return date[5:7]
  
  def getDayFromDate(self, date):	#2016-11-01
    return date[8:10]
  
#date = DateData()
#print date.year