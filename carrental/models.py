# Libraries
from django.db import models
from django import forms
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256



# User Model - Car Rental Project
class User(models.Model):
	# Enum for gender choices
	MALE = 'M'
	FEMALE = 'F'
	NOT_SPECIFIED = 'N'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(NOT_SPECIFIED, 'Not Specified'),
	)
	# Enum for state choices
	QUEENSLAND = 'QLD'
	NEW_SOUTH_WALES = 'NSW'
	SOUTH_AUSTRALIA = 'SA'
	TASMANIA = 'TAS'
	VICTORIA = 'VIC'
	STATE_CHOICES = (
		(QUEENSLAND, 'QLD'),
		(NEW_SOUTH_WALES, 'NSW'),
		(SOUTH_AUSTRALIA, 'SA'),
		(TASMANIA, 'TAS'),
		(VICTORIA, 'VIC'),
	)

	# Columns in the User model
	id = models.AutoField(primary_key=True)
	email = models.EmailField(blank = False, null = False)
	password = models.CharField(max_length = 256, blank = False, null = False)
	name = models.CharField(max_length = 50, blank = False, null = False)
	gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, blank = False, null = False)	
	birthday = models.DateField(auto_now = False, auto_now_add = False)
	address = models.CharField(max_length = 200, blank = False, null = False)



# Car Model - Car Rental Project
class Car(models.Model):	
	# Enum for drive choices
	REAR_WD = 'RWD'
	FORWARD_WD = 'FWD'
	ALL_WD = 'AWD'
	FOUR_WD = '4WD'	
	DRIVE_CHOICES = (
		(REAR_WD, 'RWD'),
		(FORWARD_WD, 'FWD'),
		(ALL_WD, 'AWD'),
		(FOUR_WD, '4WD'),
	)

	# Columns in the Car model
	car_id = models.AutoField(primary_key = True, null = False)
	makename = models.CharField(max_length = 50, blank = True, null = False)
	model = models.CharField(max_length = 50, blank = True, null = False)
	series = models.CharField(max_length = 100, blank = True, null = False)
	series_year = models.IntegerField(blank = True, null = False)
	price_new = models.IntegerField(blank = True, null = False)
	engine_size = models.DecimalField(max_digits = 3, decimal_places = 1, blank = True, null = False)
	fuel_system = models.CharField(max_length = 100, blank = True, null = False)
	tank_capacity = models.IntegerField(blank = True, null = False)
	horse_power = models.IntegerField(blank = True, null = False)
	seating = models.IntegerField(blank = True, null = False)
	standardtransmission = models.CharField(max_length = 20, blank = True, null = False)
	bodytype = models.CharField(max_length = 50, blank = True, null = False)
	drivetype = models.CharField(max_length = 3, choices = DRIVE_CHOICES, blank = True, null = False)
	wheelbase = models.IntegerField(blank = True, null = False)



# Store Model - Car Rental Project
class Store(models.Model):
	# Enum for state choices
	QUEENSLAND = 'QLD'
	NEW_SOUTH_WALES = 'NSW'
	SOUTH_AUSTRALIA = 'SA'
	TASMANIA = 'TAS'
	VICTORIA = 'VIC'
	STATE_CHOICES = (
		(QUEENSLAND, 'QLD'),
		(NEW_SOUTH_WALES, 'NSW'),
		(SOUTH_AUSTRALIA, 'SA'),
		(TASMANIA, 'TAS'),
		(VICTORIA, 'VIC'),
	)

	# Columns in the Store model
	store_id = models.AutoField(primary_key = True, null = False)	
	phone = models.CharField(max_length = 10, blank = False, null = False)
	address = models.CharField(max_length = 200, blank = False, null = False)
	state = models.CharField(max_length = 3, choices = STATE_CHOICES, blank = True, null = False)
	city = models.CharField(max_length = 200, blank = True, null = False)



# StoreGarage Model - Car Rental Project
class StoreGarage(models.Model):
	# Primary keys in both the Store and Car models
	store_id = models.IntegerField(null = True)
	car_id = models.IntegerField(null = True)