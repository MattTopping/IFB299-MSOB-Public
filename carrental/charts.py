# charts.py
from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from .models import *
import random

class buildMakeDistributionPie(Chart):
    chart_type = 'pie' 

    def get_labels(self, **kwargs):   
    	makeList = []
    	cars = Car.objects.all()

        #Build a list with only one occurance of each item in the targeted col
    	for car in cars:
    		if car.makename not in makeList:
    			makeList.append(car.makename)
    	return makeList

    def get_datasets(self, **kwargs):
		makeList = []
		cars = Car.objects.all()

        #Build a list with only one occurance of each item in the targeted col
		for car in cars:
			if car.makename not in makeList:
				makeList.append(car.makename)

        #Build the data that wants to be obtained into the same index as the label array so that they align
		buildData = []

		for make in makeList:
			carTotal = 0
			for car in cars:
				if make == car.makename:
					carTotal=carTotal+1

			buildData.append(carTotal)

		currColourList =[]

        #Dynamically generate rnd colours to the number of labels fetch from the db
		for colour in buildData:
			randColourOne =random.randint(0, 255)
			randColourTwo =random.randint(0, 255)
			randColourThree =random.randint(0, 255)
			
			currColourList.append(rgba(randColourOne, randColourTwo, randColourThree, 1))

		return [DataSet(data=buildData,
                        backgroundColor=currColourList,
                        hoverBackgroundColor=currColourList)]


class buildCarPerStoreBar(Chart):
    chart_type = 'bar'

    def get_labels(self, **kwargs):
    	stateList = []
    	stores = Store.objects.all()

        #Build a list with only one occurance of each item in the targeted col
    	for store in stores:
    		if store.state not in stateList:
    			stateList.append(store.state)
    	return stateList


    def get_datasets(self, **kwargs):
    	stateList = []
    	stores = Store.objects.all()
    	garage = StoreGarage.objects.all()

        #Build a list with only one occurance of each item in the targeted col
    	for store in stores:
    		if store.state not in stateList:
    			stateList.append(store.state)

        #Build the data that wants to be obtained into the same index as the label array so that they align
    	carCountPerState = []

    	for state in stateList:
    		currCarTotal = 0
    		for car in garage:
    			for store in stores:
    				if car.store_id == store.store_id:
    					if store.state == state:
    						currCarTotal = currCarTotal + 1

    		carCountPerState.append(currCarTotal)
			
        #Dynamically generate rnd colours to the number of labels fetch from the db
    	currColourList = []

    	for colour in carCountPerState:
			randColourOne = random.randint(0, 255)
			randColourTwo = random.randint(0, 255)
			randColourThree = random.randint(0, 255)
			currColourList.append(rgba(randColourOne, randColourTwo, randColourThree, 0.2))

        return [DataSet(data=carCountPerState,
                        label = "Values showing cars available per state",
                        borderWidth=1,
                        backgroundColor=currColourList,
                        borderColor=currColourList,)]


class buildBodyDistributionBar(Chart):
    chart_type = 'bar' 

    def get_labels(self, **kwargs):   
        bodytypeList = []
        cars = Car.objects.all()

        for car in cars:
            if car.bodytype not in bodytypeList:
                bodytypeList.append(car.bodytype)

        return bodytypeList

    def get_datasets(self, **kwargs):
        bodytypeList = []
        cars = Car.objects.all()

        #Build a list with only one occurance of each item in the targeted col
        for car in cars:
            if car.bodytype not in bodytypeList:
                bodytypeList.append(car.bodytype)

        #Build the data that wants to be obtained into the same index as the label array so that they align
        buildData = []

        for bodytype in bodytypeList:
            bodytypeTotal = 0
            for car in cars:
                if bodytype == car.bodytype:
                    bodytypeTotal=bodytypeTotal+1

            buildData.append(bodytypeTotal)

        #Dynamically generate rnd colours to the number of labels fetch from the db
        currColourList =[]

        for colour in buildData:
            randColourOne =random.randint(0, 255)
            randColourTwo =random.randint(0, 255)
            randColourThree =random.randint(0, 255)
            
            currColourList.append(rgba(randColourOne, randColourTwo, randColourThree, 0.2))

        return [DataSet(data=buildData,
                        label = "Values showing bodytype distribution available for customers",
                        borderWidth=1,
                        backgroundColor=currColourList,
                        hoverBackgroundColor=currColourList)]