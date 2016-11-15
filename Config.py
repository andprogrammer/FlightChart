#!/usr/bin/python
from Curriences import ( 
  EUR, CZK, PLN, HUF, GBP, USD, BYR, RUB,
)
from Airports import KRAKOW, LONDON


#General settings
IS_DEBUG_MODE_SET = True
SAVE_FLIGHTS_FARES_TO_FILE = True
DESTINATION_DIRECTORY_WITH_PLOTS = "Plots"
DESTINATION_DIRECTORY_WITH_FARES = "Fares"

#Flights settings
DUMMY_DEPARTURE_AND_ARRIVAL_DATE = "1999-05-06"	#CONST VARIABLE-NOT CHANGE-It is automatically changing by the program

IS_ONE_WAY = "oneway"				#oneway or return
SOURCE_AIRPORT = KRAKOW
DESTINATION_AIRPORT = LONDON
NUMBER_OF_ADULTS = 1
NUMBER_OF_CHILDREN = 0
NUMBER_OF_INFANTS = 0
MAX_CHANGES = 0					#0-only direct flights
CURRENCY = PLN
URL_REQUEST = "http://www.azair.eu/azfin.php?tp=0&searchtype=flexi&srcAirport=" + SOURCE_AIRPORT + "+%5BKRK%5D&srcTypedText=krak&srcFreeTypedText=&srcMC=&srcFreeAirport=&dstAirport=" + DESTINATION_AIRPORT + "+%5BSTN%5D&dstTypedText=london&dstFreeTypedText=&dstMC=&adults=" + str(NUMBER_OF_ADULTS) + "&children=" + str(NUMBER_OF_CHILDREN) + "&infants=" + str(NUMBER_OF_INFANTS) + "&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&dstFreeAirport=&depdate=" + DUMMY_DEPARTURE_AND_ARRIVAL_DATE + "&arrdate=" + DUMMY_DEPARTURE_AND_ARRIVAL_DATE + "&minDaysStay=1&maxDaysStay=1&nextday=0&autoprice=true&currency=" + CURRENCY + "&wizzxclub=false&supervolotea=false&schengen=false&transfer=false&samedep=true&samearr=true&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&maxChng=" + str(MAX_CHANGES) + "&isOneway=" + IS_ONE_WAY + "&resultSubmit=Search"

#Plot settings
DAYS_SHIFTER = 1				#after x days from current day start creating the plot
PERIOD = 3					    #generete plot for (PERIOD - 1) days
SLEEP_TIME = 2					#sleep time prevent suspicion of web scraping
PLOT_WIDTH = 2500
PLOT_HEIGHT = 1000
PLOT_PPI = 72
