# Libraries
from django import forms
from django.forms.extras import widgets
from passlib.hash import pbkdf2_sha256

# Car Rental files (models.py)
from .models import SignUp, User, Car


# Test form
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		# Put in order
		fields = ['full_name', 'email'] 
		
	# Python functions to help with validation
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid edu email")
		return email


# Sign up form - Car Rental Project
class UserForm(forms.ModelForm):	
	# Presenting the password fields properly
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	
	# Loading in the model
	class Meta: 
		# Setting the field 'model' to the database User
		model = User
		# Selecting the fields that are being shown on the form	
		fields = ['email', 'password', 'password2', 'name', 'gender', 'birthday', 'address']	
		# Adding details to specific fields
		widgets = {			
			'email': forms.TextInput(attrs = {'placeholder': 'Insert email here'}),		
			# Making the birthday field a date picker
			'birthday': forms.DateInput(attrs = {'class': 'datepicker'}),
		}	

	# Password match functionality
	def clean(self):
		# Cleaning the data from the user form
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get("password2")

		# Checking if the passwords are different
		if password != password2:
			# If they are, raise an error saying they don't match
			raise forms.ValidationError(
				"Passwords don't match"
			)


class CarForm(forms.ModelForm):
	# Loading in the model
	class Meta: 
		model = Car
		fields = ['makename', 'model', 'series', 'series_year', 'price_new', 'engine_size', 'fuel_system', 
		'tank_capacity', 'horse_power', 'seating', 'standardtransmission', 'bodytype', 'drivetype', 'wheelbase']	


class SignInForm(forms.ModelForm):
	# Presenting the password fields properly
	password = forms.CharField(widget = forms.PasswordInput)

	# Loading in the model
	class Meta: 
		model = User
		fields = ['email', 'password']	

	def clean(self):		
		# Get the email and password from the form
		cleaned_data = super(SignInForm, self).clean()
		email = cleaned_data.get("email")
		password = cleaned_data.get("password")
		users = User.objects.all()

		emailConfirmed = False	
		userConfirmed = False	

		for user in users:
			if user.email == email:	
				emailConfirmed = True

				ver = pbkdf2_sha256.verify(password, user.password)
				if userConfirmed == False and ver == True:
					print("yeahnahyeah!")
					userConfirmed = True
					#use set function to login user
					break
		
		if emailConfirmed == False:
			raise forms.ValidationError("Email not found.")
		elif emailConfirmed == True and userConfirmed == False:
			raise forms.ValidationError("Incorrect password.")
	
