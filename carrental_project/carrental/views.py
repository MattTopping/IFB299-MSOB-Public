# Libraries
from django import forms
from .globals import changeLoginState, returnLoginState
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template import Context, loader
from passlib.hash import pbkdf2_sha256

# Car Rental files (forms.py and models.py)
from .forms import SignUpForm, UserForm, CarForm, SignInForm
from .models import User, Car


# Home page - Car Rental
def index(request):
	# Loading in all of the results	
	form = CarForm(request.GET)		
	# Set cars to be all of the car objects
	cars = Car.objects.all()

	# If the form is valid
	if form.is_valid():		
		# If the field had elements in it, change the return to include them
		if form.cleaned_data["makename"]:
			cars = cars.filter(makename=form.cleaned_data["makename"])
		elif form.cleaned_data["model"]:
			cars = cars.filter(model=form.cleaned_data["model"])
		elif form.cleaned_data["series"]:
			cars = cars.filter(series=form.cleaned_data["series"])			
		elif form.cleaned_data["series_year"]: 
			cars = cars.filter(series_year=form.cleaned_data["series_year"])
		elif form.cleaned_data["price_new"]:
			cars = cars.filter(price_new=form.cleaned_data["price_new"])
		elif form.cleaned_data["engine_size"]:
			cars = cars.filter(engine_size=form.cleaned_data["engine_size"])
		elif form.cleaned_data["fuel_system"]:
			cars = cars.filter(fuel_system=form.cleaned_data["fuel_system"])
		elif form.cleaned_data["tank_capacity"]:
			cars = cars.filter(tank_capacity=form.cleaned_data["tank_capacity"])
		elif form.cleaned_data["horse_power"]:
			cars = cars.filter(horse_power=form.cleaned_data["horse_power"])
		elif form.cleaned_data["seating"]:
			cars = cars.filter(seating=form.cleaned_data["seating"])
		elif form.cleaned_data["standardtransmission"]:
			cars = cars.filter(standardtransmission=form.cleaned_data["standardtransmission"])
		elif form.cleaned_data["bodytype"]:
			cars = cars.filter(bodytype=form.cleaned_data["bodytype"])
		elif form.cleaned_data["drivetype"]:
			cars = cars.filter(drivetype=form.cleaned_data["drivetype"])
		elif form.cleaned_data["wheelbase"]:
			cars = cars.filter(wheelbase=form.cleaned_data["wheelbase"])

		print(cars)		

	# Change the context to include the table with results
	context = {
		"form": form, 
		"car_list": cars,
	}

	# Render the page	
	return render(request, "carrental/index.html", context)


# Signup page - Car Rental
def signup(request):
	# Guidance for the user
	title = "User Registration"

	if request.method == 'POST':
		# Imports the form
		form = UserForm(request.POST)				

		# If the form posted has passed all validation
		if form.is_valid():
			# List everything that is being posted
			email = request.POST['email']
			password = request.POST['password']
			# Encrypt the password for the database
			enc_password = pbkdf2_sha256.encrypt(password, rounds = 12000, salt_size = 32)		
			password2 = request.POST['password2']
			enc_password2 = pbkdf2_sha256.encrypt(password2, rounds = 12000, salt_size = 32)
			name = request.POST['name']
			gender = request.POST['gender']
			birthday = request.POST['birthday']
			address = request.POST['address']

			# Creates the object that is then sent through to the database
			User.objects.create(
				email = email,
				# Sets the password to the encrypted version
				password = enc_password,
				name = name, 
				gender = gender, 
				birthday = birthday,
				address = address		
			)

			# Changes the title to let the user know their account was created
			context = {
				"title": "Successful! You can now log in."
			}

		# Specifies to show this content
		context = {
			"title": title,
			"form": form,
		}

		# Render the page
		return render(request, "carrental/sign-up.html", context)

	else:
		form = UserForm()
		
		users = User.objects.all().filter(name = "abc", email = "test2@test.test")
		
		context = {
			"form": form,
			"users": users,
		}

		# Render the page
		return render(request, "carrental/sign-up.html", context)


# Signin page - Car Rental
def signin(request):
	if request.method == 'POST':
		# Imports the form and all of the existing users
		form = SignInForm(request.POST)			

		# If the form is valid
		if form.is_valid():
			changeLoginState(True)
			return redirect("/testsearch/")
			
	else: 
		form = SignInForm()

	# Render the page
	return render(request, "carrental/sign-in.html", {"form": form})	