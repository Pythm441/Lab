#Example1 
'''
class car:
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def honk(self):
        print("Beeb BEEB")    

my_car = car("Skoda", "Grey")
print(my_car.brand)
print(my_car.color)
my_car.honk()
'''

'''
def greet():
  print("Welcome!")

#list
prices = [55, 68, 77, 36]

#data types
x = 5
city = "London"
is_open = True


print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))
'''
'''
class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
    
# Creating an instance
my_dog = Dog("Bob")

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()

'''


'''
#parent class
class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type
  
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name,type, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name, type)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax","Predator", "Bulldog", 5)
#inherited attribute
print(my_dog.name)
print(my_dog.type)
#Additional attributes
print(my_dog.breed)
print(my_dog.age)

'''

'''
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

# Using overridden methods
my_dog.sound()
my_cat.sound()
'''
'''
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")

# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)

# Calling the overridden sound method
my_dog.sound()

'''


#Polymorphisim
'''
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

animals = [my_dog, my_cat]

for animal in animals:
  animal.sound()

'''

'''
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self.__odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()
my_car.__odometer = 0  #It won't change it since it is a private attribute. 
my_car.read_odometer()

#Can be accessed through name mangling

my_car.__odometer = 0
print(my_car.__odometer)    #it can be used for methods also

'''
'''
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()  #it can be changed since it is not private

'''



'''
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)
'''

#Static methods
'''
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #staticmethod
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# calling the static method
Book.books_in_series("Harry Potter", 7)
'''