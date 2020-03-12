# Libraries
from django import forms
from django.views.generic import View, FormView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from passlib.hash import pbkdf2_sha256

# Car Rental Files
from .forms import UserForm, CarForm, CarFormLocation, SignInForm
from .models import User, Car, Store, StoreGarage
from .charts import *



# Home Page - Car Rental Project
def index(request):
	# Loading in all of the results	
	form_car = CarForm(request.GET)		
	form_loc = CarFormLocation(request.GET)

	# Set cars, stores and storegarage to be all objects from each
	cars = Car.objects.all()
	stores = Store.objects.all() 
	storegarage = StoreGarage.objects.all()		

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	# If the form is valid
	if form_loc.is_valid():	
		# Used to contain filter results
		valid_stores = []
		valid_cars = []

		# Gathering all of the cleaned form data
		city_form=form_loc.cleaned_data["city"]
		state_form=form_loc.cleaned_data["state"]		
		
		# If the field had elements in it, change the return to include them
		if form_loc.cleaned_data["city"]:
			stores = stores.filter(city__istartswith = city_form)
		if form_loc.cleaned_data["state"]:
			stores = stores.filter(state = state_form)

		# Append the valid store ids into valid_stores
		for store in stores: 
			valid_stores.append(store.store_id)
		
		# Remove all other stores from the storegarage QuerySet
		for garage in storegarage:
			if garage.store_id not in valid_stores:
				storegarage = storegarage.exclude(store_id = garage.store_id)

		# Append all the valid cars in those stores to valid_cars
		for car in storegarage: 
			if car.car_id not in valid_cars:
				valid_cars.append(car.car_id)		

		# Remove all other cars from the cars QuerySet
		for car in cars: 
			if car.car_id not in valid_cars:
				cars = cars.exclude(car_id = car.car_id)

	# If the form is valid
	if form_car.is_valid():		
		# Gathering all of the cleaned form data
		makename_form=form_car.cleaned_data["makename"]
		model_form=form_car.cleaned_data["model"]
		series_form=form_car.cleaned_data["series"]
		series_year_form=form_car.cleaned_data["series_year"]
		price_new_form=form_car.cleaned_data["price_new"]
		engine_size_form=form_car.cleaned_data["engine_size"]
		fuel_system_form=form_car.cleaned_data["fuel_system"]
		tank_capacity_form=form_car.cleaned_data["tank_capacity"]
		horse_power_form=form_car.cleaned_data["horse_power"]
		standardtransmission_form=form_car.cleaned_data["standardtransmission"]
		bodytype_form=form_car.cleaned_data["bodytype"]
		drivetype_form=form_car.cleaned_data["drivetype"]
		wheelbase_form=form_car.cleaned_data["wheelbase"]

		# If the field had elements in it, change the return to include them
		if form_car.cleaned_data["makename"]:
			cars = cars.filter(makename__istartswith = makename_form)
		if form_car.cleaned_data["model"]:
			cars = cars.filter(model__istartswith = model_form)
		if form_car.cleaned_data["series"]:
			cars = cars.filter(series__istartswith = series_form)			
		if form_car.cleaned_data["series_year"]: 
			cars = cars.filter(series_year__istartswith = series_year_form)
		if form_car.cleaned_data["price_new"]:
			cars = cars.filter(price_new__istartswith = price_new_form)
		if form_car.cleaned_data["engine_size"]:
			cars = cars.filter(engine_size__istartswith = engine_size_form)
		if form_car.cleaned_data["fuel_system"]:
			cars = cars.filter(fuel_system__istartswith = fuel_system_form)
		if form_car.cleaned_data["tank_capacity"]:
			cars = cars.filter(tank_capacity__istartswith = tank_capacity_form)
		if form_car.cleaned_data["horse_power"]:
			cars = cars.filter(horse_power__istartswith = horse_power_form)
		if form_car.cleaned_data["seating"]:
			cars = cars.filter(seating=form.cleaned_data["seating"])
		if form_car.cleaned_data["standardtransmission"]:
			cars = cars.filter(standardtransmission__istartswith = standardtransmission_form)
		if form_car.cleaned_data["bodytype"]:
			cars = cars.filter(bodytype__istartswith = bodytype_form)
		if form_car.cleaned_data["drivetype"]:
			cars = cars.filter(drivetype__istartswith = drivetype_form)
		if form_car.cleaned_data["wheelbase"]:
			cars = cars.filter(wheelbase__istartswith = wheelbase_form)

	# Change the context to include the table with results
	context = {
		"form_car": form_car, 
		"form_loc": form_loc,
		"car_list": cars,
		"store_list": stores,
		# Send session information to HTML
		"sessionEmail": sessionEmail,
		"sessionAdmin": sessionAdmin,
	}

	# Render the page	
	return render(request, "carrental/index.html", context)



# Signup Page - Car Rental Project
def signup(request):
	# Guidance for the user
	title = "Sign Up"

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	if request.method == 'POST':
		# Imports the form
		form = UserForm(request.POST)	

		# Specifies to show this content
		context = {
			"title": title,
			"form": form,
			# Send session information to HTML
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
		}	

		currentUsers = User.objects.all()

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

			# Changes the title to let the user know their account was created
			context = {
				"title": "Successful! You can now log in.",
				# Send session information to HTML
				"sessionEmail": sessionEmail,
				"sessionAdmin": sessionAdmin,
			}	

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

		# Render the page
		return render(request, "carrental/sign-up.html", context)

	else:
		form = UserForm()		
		users = User.objects.all().filter(name = "abc", email = "test2@test.test")
		
		context = {
			"title": title,
			"form": form,
			"users": users,
			# Send session information to HTML
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
		}

		# Render the page
		return render(request, "carrental/sign-up.html", context)



# Signin Page - Car Rental Project
def signin(request):
	title = "Sign In"

	# Define default values
	email = None
	form = SignInForm()	
 
	# If the page is not posting information 
	if request.method == 'GET':
		# If a logout has be requested (not none)
		if request.GET.get("logoutRequest") == "Logout":
			# If there is a session that is currently valid
			if request.session.has_key('username'):
				# Remove current session and redirect to index
				request.session.flush()
				return redirect("index")

		# If there is a current session, store username
		if 'username' in request.session:
			email = request.session['username']

	# If logging in
	elif request.method == 'POST':
		# Imports the form and all of the existing users
		form = SignInForm(request.POST)	

		# If the form is valid
		if form.is_valid():
			# Store username for session
			email = form.cleaned_data["email"]

			# Create Session
			request.session['username'] = email

			# Redirect to home page
			return redirect('index')

	# Default load state to catch bugs	
	else: 		
		form = SignInForm()

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	context = {
		"title": title,
		"form": form,
        "email": email,
        # Send session information to HTML
        "sessionEmail": sessionEmail,
        "sessionAdmin": sessionAdmin,
    }

	# Render the page
	return render(request, "carrental/sign-in.html", context)



# Car Specifications Page - Car Rental Project
def car_desc(request, id):
	# Gets the car by ID reference
	instance = get_object_or_404(Car, car_id = id)

	# Create the lists for stores
	stores = []
	availableStores = []
	
	# Retrieve all of the stores that match the car id
	storeID = StoreGarage.objects.all()
	storeID = storeID.filter(car_id = instance.car_id)

	# Add all of the store id's to a list
	for ID in storeID:
		availableStores.append(ID.store_id)		

	# All of of the store objects to a list
	for store in availableStores:	
		stores.append(Store.objects.get(store_id = store))

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	# Specifies what is being included on template
	context = {
		"title": instance.makename,
		"instance": instance,
		"stores": stores,
		# Send session information to HTML
		"sessionEmail": sessionEmail,
		"sessionAdmin": sessionAdmin,
	}

	# Render the page
	return render(request, "carrental/car.html", context)



# Store Stock Page - Car Rental Project
def store_stock(request, id):
	# Gets the store by ID reference
	instance = get_object_or_404(Store, store_id = id)

	# Set cars and storegarage to be all objects from each
	cars = Car.objects.all()	
	storegarage = StoreGarage.objects.all()	
	# Used to store cars in relation to the store
	store_cars = []

	# Filter storegarage to only include cars with current store id
	storegarage = storegarage.filter(store_id = instance.store_id)

	# Append all the valid cars in those stores to valid_cars
	for car in storegarage: 
		if car.car_id not in store_cars:
			store_cars.append(car.car_id)		

	# Remove all other cars from the cars QuerySet
	for car in cars: 
		if car.car_id not in store_cars:
			cars = cars.exclude(car_id = car.car_id)

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	# Specifies what is being included on template
	context = {		
		"instance": instance,
		"cars": cars,
		# Send session information to HTML
		"sessionEmail": sessionEmail,
		"sessionAdmin": sessionAdmin,
	}

	# Render the page
	return render(request, "carrental/store.html", context)



# Functionality: Checks if admin is logged in on each page - Car Rental Project
def adminChecker(input, request):
	email_base, provider = input.split("@")
	if provider == "carrental.com":
		return True
	else:
		return False



# Functionality: 
def analysisLoad(request):
	email = None
	graph = None

	if 'username' in request.session:
		currentEmail = request.session['username']
		if adminChecker(currentEmail, request):
			email = currentEmail
			print("Welcome!")
		else:
			email = "Access Denied"
			print("Access Not Allowed")
	else:
		print("Please Login")

	# Running session fetching function to prep variable for HTML passing
	sessionEmail = navbarSessionPasser(request)
	sessionAdmin = navbarAdminPasser(request)

	context = {}

	#Graph loading logic
	if request.GET.get("graphRequest") == "View Tool One":
		context = {
			"email": email,
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
			"graph": "toolOne",
			"generateGraph": buildMakeDistributionPie(),
		}
	elif request.GET.get("graphRequest") == "View Tool Two":
		context = {
			"email": email,
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
			"graph": "toolTwo",
			"generateGraph": buildCarPerStoreBar(),
		}
	elif request.GET.get("graphRequest") == "View Tool Three":
		context = {
			"email": email,
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
			"graph": "toolThree",
			"generateGraph": buildBodyDistributionBar(),
		}
	else:
		graph = None
		context = {
			"email": email,
			"sessionEmail": sessionEmail,
			"sessionAdmin": sessionAdmin,
			"graph": "none",
		}

	return render(request, "carrental/analysisAdmin.html", context)



# Functionality: Checks whether there is a current session or not - Car Rental Project
def navbarSessionPasser(request):
	if 'username' in request.session:
		return request.session['username']
	else: 
		return None



# Functionality: Checks if an admin is logged into the current session - Car Rental Project
def navbarAdminPasser(request):
	if 'username' in request.session:
		username = request.session['username']
		if adminChecker(username, request):
			return True
		else:
			return False
	else: 
		return False