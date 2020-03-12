# Libraries
from django.test import TestCase
from passlib.hash import pbkdf2_sha256

# Car Rental Files
from .models import User, Car, Store, StoreGarage



# User Model Testing - Car Rental Project
class UserTestCase(TestCase):
    # Create users 
    def setUp(self):
        User.objects.create(email = "test@test.com", password = "test", name = "test", gender = "M", birthday = "2018-09-09", 
                            address = "14th Test Test")
        User.objects.create(email = "test2@test.com", password = "test2", name = "test2", gender = "F", birthday = "2018-10-09", 
                            address = "15th Test Test")        
    
    # Testing that the user objects are being assigned correctly
    def test_user_assignment(self):
        # Assign user
        user1 = User.objects.get(name = "test")

        # Run tests   
        self.assertEqual(user1.email, "test@test.com")
        self.assertEqual(user1.name, "test")
        self.assertEqual(user1.gender, 'M')
        self.assertEqual(user1.birthday.strftime("%Y-%m-%d"), "2018-09-09")
        self.assertEqual(user1.address, "14th Test Test")
    
    # Testing that the users are being assigned correctly
    def test_two_user_assignment(self):
        # Assign users
        user1 = User.objects.get(name = "test")
        user2 = User.objects.get(name = "test2")
        
        # Run tests
        self.assertNotEqual(user1.id, user2.id)
        self.assertNotEqual(user1.name, user2.name)
        self.assertNotEqual(user1.gender, user2.gender)
        self.assertNotEqual(user1.birthday, user2.birthday)
        self.assertNotEqual(user1.address, user2.address)
    
    # Testing that the user passwords are being salted correctly
    def test_password_setting(self):
        # Assign users
        user1 = User.objects.get(name = "test")
        user2 = User.objects.get(name = "test2")

        # Salt the passwords
        enc_password = pbkdf2_sha256.encrypt(user1.password, rounds = 12000, salt_size = 32)
        enc_password2 = pbkdf2_sha256.encrypt(user1.password, rounds = 12000, salt_size = 32)
        enc_password3 = pbkdf2_sha256.encrypt(user2.password, rounds = 12000, salt_size = 32)

        # Unencrypt password
        boolean = pbkdf2_sha256.verify("test", enc_password)

        # Check that the password is encrypted correctly
        self.assertNotEquals(enc_password, "test")
        # Check that the password encryption is different each time
        self.assertNotEqual(enc_password, enc_password2)
        self.assertNotEqual(enc_password, enc_password3)
        # Check that the salted password can be read / converted back
        self.assertEqual(boolean, True)    

    # Testing that there is no user duplication
    def test_user_account_duplication(self):
       # User enters an email as such in the form. 
        email = "test@test.com"
        
        # The filter is applied to check if email exists
        emailVal = User.objects.filter(email = email)

        # The result should be 1
        self.assertEqual(len(emailVal), 1)



# Car Model Testing - Car Rental Project
class CarTestCase(TestCase):
    # Create cars 
    def setUp(self):
        Car.objects.create(makename = "TestCar", model = "TestModel", series = "TestSeries", series_year = 1990, price_new = 20000, 
                           engine_size = 2.7, fuel_system = "TestFuelSystem", tank_capacity = 80, horse_power = 120, seating = 5, 
                           standardtransmission = "6A", bodytype = "TestBodyType", drivetype = "4WD", wheelbase = 2880)
        Car.objects.create(makename = "TestCar2", model = "ModelTest", series = "TestSeries2", series_year = 1991, price_new = 20001, 
                           engine_size = 2.7, fuel_system = "TestFuelSystem2", tank_capacity = 90, horse_power = 130, seating = 6, 
                           standardtransmission = "62A", bodytype = "TestBodyType2", drivetype = "FWD", wheelbase = 2880)
    
    # Testing that a car is assigning properly
    def test_car_assignment(self):
        # Assign car
        car = Car.objects.get(makename = "TestCar")        

        # Test that each field is set correctly
        self.assertEqual(car.car_id, 1)
        self.assertEqual(car.model, "TestModel")
        self.assertEqual(car.series, "TestSeries")
        self.assertEqual(car.series_year, 1990)
        self.assertEqual(car.price_new, 20000)
        self.assertEqual(str(car.engine_size), "2.7")
        self.assertEqual(car.fuel_system, "TestFuelSystem")
        self.assertEqual(car.tank_capacity, 80)
        self.assertEqual(car.horse_power, 120)
        self.assertEqual(car.seating, 5)
        self.assertEqual(car.standardtransmission, "6A")
        self.assertEqual(car.bodytype, "TestBodyType")
        self.assertEqual(car.drivetype, "4WD")
        self.assertEqual(car.wheelbase, 2880)
    
    # Testing that two cars are assigning properly
    def test_two_cars_assignment(self):
        # Assign cars
        car1 = Car.objects.get(makename = "TestCar")
        car2 = Car.objects.get(makename = "TestCar2")

        # Test that each field is set correctly (both are different)
        self.assertNotEqual(car1.model, car2.model)
        self.assertNotEqual(car1.series, car2.series)
        self.assertNotEqual(car1.series_year, car2.series_year)
        self.assertNotEqual(car1.price_new, car2.price_new)
        self.assertNotEqual(car1.engine_size, car2.engine_size)
        self.assertNotEqual(car1.fuel_system, car2.fuel_system)
        self.assertNotEqual(car1.tank_capacity, car2.tank_capacity)
        self.assertNotEqual(car1.horse_power, car2.horse_power)
        self.assertNotEqual(car1.seating, car2.seating)
        self.assertNotEqual(car1.standardtransmission, car2.standardtransmission)
        self.assertNotEqual(car1.bodytype, car2.bodytype)
        self.assertNotEqual(car1.drivetype, car2.drivetype)
        self.assertNotEqual(car1.wheelbase, car2.wheelbase)
    
    # Testing that filtering objects works correctly
    def test_two_cars_assignment(self):
        # Gather all car objects
        cars = Car.objects.all()
        # Filter out the second car
        cars = cars.filter(makename = "TestCar")

        # Test to see if the size has updated
        self.assertEqual(len(cars), 1)

        # Test to see if the object remaining is the first car
        car = Car.objects.get(makename = "TestCar")
        self.assertNotEqual(car, None)
    
    # Testing that filtering string objects works correctly
    def test_string_filtering(self):
        # Gather all car objects
        cars = Car.objects.all()
        # Filter out names that start with volv
        cars = cars.filter(model__istartswith = "Mo")
        MoCars = len(cars)
        self.assertEqual(MoCars, 1)
    
    # Testing that number filtering objects works correctly
    def test_number_filtering(self):
        # Gather all car objects
        cars = Car.objects.all()
        # Filter out names that start with volv
        cars = cars.filter(series_year__istartswith = 1990)
        filtCars = len(cars)
        self.assertEqual(filtCars, 1)



# Store Model Testing - Car Rental Project
class StoreTestCase(TestCase):
    # Create cars 
    def setUp(self):
        Store.objects.create(phone = 1234567890, address = "4 Test Street", state = "QLD", city = "Test1")
        Store.objects.create(phone = 9876543210, address = "5 Test Street", state = "NSW", city = "Test2")

    # Test the store is assigning correctly       
    def test_store_assignment(self):
        # Assign store
        store = Store.objects.get(city = "Test1")

        # Test fields are being set correctly        
        self.assertEqual(store.phone, str(1234567890))
        self.assertEqual(store.address, "4 Test Street")
        self.assertEqual(store.state, "QLD")
        self.assertEqual(store.city, "Test1")
    
    # Test two stores are assigning correctly
    def test_two_stores_assignment(self):
        # Assign stores
        store1 = Store.objects.get(city = "Test1")
        store2 = Store.objects.get(city = "Test2")

        # Test fields are being set correctly        
        self.assertNotEqual(store1.phone, store2.phone)        
        self.assertNotEqual(store1.address, store2.address)
        self.assertNotEqual(store1.state, store2.state)        
        self.assertNotEqual(store1.address, store2.address)        



class StoreGarageTestCase(TestCase):
     # Create cars, stores and garages
    def setUp(self):
        Store.objects.create(phone = 1234567890, address = "4 Test Street", state = "QLD", city = "Test1")
        Store.objects.create(phone = 9876543210, address = "5 Test Street", state = "NSW", city = "Test2")
        Car.objects.create(makename = "TestCar", model = "TestModel", series = "TestSeries", series_year = 1990, price_new = 20000, 
                           engine_size = 2.7, fuel_system = "TestFuelSystem", tank_capacity = 80, horse_power = 120, seating = 5, 
                           standardtransmission = "6A", bodytype = "TestBodyType", drivetype = "4WD", wheelbase = 2880)
        Car.objects.create(makename = "TestCar2", model = "TestModel2", series = "TestSeries2", series_year = 1991, price_new = 20001, 
                           engine_size = 2.7, fuel_system = "TestFuelSystem2", tank_capacity = 90, horse_power = 130, seating = 6, 
                           standardtransmission = "62A", bodytype = "TestBodyType2", drivetype = "FWD", wheelbase = 2880)
        StoreGarage.objects.create(store_id = 1, car_id = 1)
        StoreGarage.objects.create(store_id = 1, car_id = 2)
        StoreGarage.objects.create(store_id = 2, car_id = None)

    # Testing that stores are assigning properly
    def test_correct_assignments(self):
        # Assign stores
        stores1 = StoreGarage.objects.filter(store_id = 1)
        store2 = StoreGarage.objects.get(store_id = 2)

        # Run tests
        self.assertEqual(len(stores1), 2)
        self.assertEqual(stores1[0].car_id, 1)
        self.assertEqual(stores1[1].car_id, 2)
        self.assertEqual(store2.car_id, None)
