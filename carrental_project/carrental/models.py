# Libraries
from django.db import models
from django import forms
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = '120', blank = False, null = True, default = '')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	
	def __unicode__(self):
		return self.email	


# User model - Car Rental
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

	# Columns in the User model	
	email = models.EmailField(blank = False, null = False)
	password = models.CharField(max_length = 256, blank = False, null = False)
	name = models.CharField(max_length = 50, blank = False, null = False)
	gender = models.CharField(max_length = 1, choices = GENDER_CHOICES, blank = False, null = False)
	birthday = models.DateField(auto_now = False, auto_now_add = False)
	address = models.CharField(max_length = 200, blank = False, null = False)


# Car model - Car Rental
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
