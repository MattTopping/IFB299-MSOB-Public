# Libraries
from django import forms
from django.forms.extras import widgets
from passlib.hash import pbkdf2_sha256
from pygeocoder import Geocoder

# Car Rental Files
from .models import User, Car, Store



# Sign Up Form - Car Rental Project
class UserForm(forms.ModelForm):	
	# Presenting the password fields properly
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Password.'}))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Matching password.'}))
	companyPassword = forms.CharField(required = False, widget = forms.PasswordInput(attrs = 
	{'placeholder': 'Optional: Staff Account Creation.'}))
	
	# Loading in the model
	class Meta: 		
		model = User
		# Selecting the fields that are being shown on the form	
		fields = ['email', 'companyPassword', 'password', 'password2', 'name', 'gender', 'birthday', 'address']	
		# Adding details to specific fields
		widgets = {			
			'email': forms.TextInput(attrs = {'placeholder': 'Eg: example@hotmail.com'}),
			'name': forms.TextInput(attrs = {'placeholder': 'Eg. Sam'}),
			# Making the birthday field a date picker
			'birthday': forms.DateInput(attrs = {'class': 'datepicker', 'placeholder': 'Select birthday.'}),
			'address': forms.TextInput(attrs = {'placeholder': 'Eg. 4 Example Road'}),
		}	

	# Custom validation
	def clean(self):
		# Cleaning the data from the user form
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get("password2")	
		companyPassword = cleaned_data.get("companyPassword")	
		name = cleaned_data.get("name")
		address = cleaned_data.get("address")

		# Splitting the email into different segments
		email = cleaned_data.get("email")
		if email is not None:			
			email_base, provider = email.split("@")
			domain, extension = provider.split('.')
		else: 
			raise forms.ValidationError("Email can't be empty")

		# Filter current users with current email
		emailVal = User.objects.filter(email = email)

		# Split the address		
		if address is not None:	
			addressVal = address.split()
		else: 
			raise forms.ValidationError("Address can't be empty")

		# Checking if the passwords are different
		if password != password2:
			# If they are, raise an error saying they don't match
			raise forms.ValidationError("Passwords don't match")

		# Check if the password is strong or not
		elif not (any(x.isupper() for x in password) and any(x.islower() for x in password) 
    		and any(x.isdigit() for x in password) and len(password) >= 7):
			raise forms.ValidationError("The password must contain an uppercase, lowercase, number and be at least 7 digits")		
			
		# Check if the email already exists
		elif len(emailVal) != 0:
			raise forms.ValidationError("Email already exists.")

		# Check if the name starts with a capital
		elif name != None:
			if name[0].isupper() != True:
				raise forms.ValidationError("No capital at beginning of name.")
		
		# Check if the email ends in .com
		elif not extension == "com":
			raise forms.ValidationError("Please use a .com email")	

		# Check if address is correct format
		elif addressVal[0].isdigit() is False or len(addressVal) != 3:
			raise forms.ValidationError("Please enter a valid address")

		# IMPORTANT: Checks whether user inputted correct company password
		if provider == "carrental.com":
			if companyPassword != "carrental":
				raise forms.ValidationError("Company password incorrect")



# Index Search Form (main section) - Car Rental Project
class CarForm(forms.ModelForm):
	# Loading in the model
	class Meta: 
		model = Car
		fields = ['makename', 'model', 'series', 'series_year', 'price_new', 'engine_size', 'fuel_system', 
		'tank_capacity', 'horse_power', 'seating', 'standardtransmission', 'bodytype', 'drivetype', 'wheelbase']



# Index Search Form (end section) - Car Rental Project
class CarFormLocation(forms.ModelForm):
	# Loading in the model
	class Meta: 
		model = Store
		fields = ['city', 'state']



# Sign In Form - Car Rental Project
class SignInForm(forms.ModelForm):
	# Presenting the password fields properly
	password = forms.CharField(widget = forms.PasswordInput)

	# Loading in the model
	class Meta: 
		model = User
		fields = ['email', 'password']	

	# Custom validation
	def clean(self):		
		# Get the email and password from the form
		cleaned_data = super(SignInForm, self).clean()
		email = cleaned_data.get("email")
		password = cleaned_data.get("password")
		users = User.objects.all()

        # Test case variables
		emailConfirmed = False	
		userConfirmed = False	

		# Checks if the user has entered a password first
		if password == None: 
			raise forms.ValidationError("Please enter a password.")
		else:
			# Search through the usernames in the database
			for user in users:
				# If the username exists
				if user.email == email:	
					emailConfirmed = True
					# Check if the password matches the email
					ver = pbkdf2_sha256.verify(password, user.password)
					# If they do match confirm that user is good to sign in
					if userConfirmed == False and ver == True:
						userConfirmed = True
						break

		# Generate error messages based off test case variables
		if emailConfirmed == False:
			raise forms.ValidationError("Email not found.")
		elif emailConfirmed == True and userConfirmed == False:
			raise forms.ValidationError("Incorrect password.")