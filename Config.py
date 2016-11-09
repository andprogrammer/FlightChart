#!/usr/bin/python


IS_DEBUG_MODE_SET = True
SAVE_FLIGHTS_FARES_TO_FILE = True
DESTINATION_DIRECTORY_WITH_PLOTS = "Plots"
DESTINATION_DIRECTORY_WITH_FARES = "Fares"
DUMMY_DEPARTURE_AND_ARRIVAL_DATE = "1999-05-06"	#used in URL_REQUEST variable
URL_REQUEST = "http://www.azair.eu/azfin.php?tp=0&searchtype=flexi&srcAirport=Krakow+%5BKRK%5D&srcTypedText=krak&srcFreeTypedText=&srcMC=&srcFreeAirport=&dstAirport=London+%5BSTN%5D&dstTypedText=london&dstFreeTypedText=&dstMC=&adults=1&children=0&infants=0&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&dstFreeAirport=&depdate=" + DUMMY_DEPARTURE_AND_ARRIVAL_DATE + "&arrdate=" + DUMMY_DEPARTURE_AND_ARRIVAL_DATE + "&minDaysStay=1&maxDaysStay=1&nextday=0&autoprice=true&currency=PLN&wizzxclub=false&supervolotea=false&schengen=false&transfer=false&samedep=true&samearr=true&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&maxChng=0&isOneway=oneway&resultSubmit=Search"
DAYS_SHIFTER = 1				#after x days from current day start creating the plot
PERIOD = 7					#generete plot for (PERIOD - 1) days
SLEEP_TIME = 2					#sleep time prevent suspicion of web scraping
PLOT_WIDTH = 2500
PLOT_HEIGHT = 1000
PLOT_PPI = 72
