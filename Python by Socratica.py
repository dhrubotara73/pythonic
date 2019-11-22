# hello world in python
# print("Hello World!")
#
# python strings
# message = "meet me tonight"
# print(message)
# message2 = 'the clock strikes at midnight'
# print(message2)
# message3 = 'i\'m looking for someone to share in an adventure'
# print(message3)
# message4 = message3 = "i'm looking for someone to share in an adventure"
# print(message4)
# message5 = 'the phrase "Beam me up, Scotty" was never said in Star Trek.'
# print(message5)
# movie_quote = """One of my favourite lines from Godfather is:
# "I' am going to make him an offer he can't refuse."
# Do you know who said this?"""
# print(movie_quote)
#
# numbers in python version 3
# types of numbers: int, float, complex
#
# int
# a = 496
# print(type(a))
# print(a)
#
# float
# e = 2.718281828
# print(type(e))
# print(e)
#
# complex
# z = 3 + 4j
# print(type(z))
# print(z.real)
# print(z.imag)
# print(z)

# arithmetic in python 3
# x = 28
# y = 28.0
# print(float(x))
# print(int(3.14))
# x1 = 1.732 + 0j
# print(x1)
# x2 = complex(1.732)
# print(x2)

# a = 2
# b = 6.0
# c = 12 + 0j
# print(a + b)
# print(b - a)
# print(a * b)
# print(a * 7)
# print(c/b)
# print(16/5)
# print(20/5)
# print(16 % 5)
# print(16//5)

# interactive help

# print(dir())
# print(dir(__builtins__))
# help(pow)
# print(pow(2, 10))
# print(2**10)
# print(dir(__builtins__))
# help(hex)
# print(hex(10))  # returns integer in python 3
# print(hex(15))
# print(hex(10) + hex(15))
# print(0x15)  # hex to decimal
# print(0x10)  # hex to decimal

# list of modules
# help('modules')

# import math
# print(dir())
# print(dir(math))
# help(math.radians)
# print(math.radians(180))
# print(math.radians(90))
# print(math.radians(45))

# print(True)
# print(type(True))
# print(False)
# print(type(False))
# a = 3
# b = 5
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
#
# print(bool(28))
# print(bool(-2.71828))
# print(bool(0))
# print(bool("Turing"))
# print(bool(" "))
# print(bool(""))
# print(str(True))
# print(str(False))
# print(int(True))
# print(int(False))
# print(5 + True)
# print(10 * False)

# import datetime
# print(dir(datetime))
# help(datetime.date)
# gvr = datetime.date(1956, 1, 31)
# print(gvr)
# print(gvr.year)
# print(gvr.month)
# print(gvr.day)
# print(dir(datetime))
# mill = datetime.date(2000, 1, 1)  # crazy day
# dt = datetime.timedelta(100)
# print(mill + dt)
# print(mill - dt)
#
# Day-Name, Month-name Day-#, Year
# print(gvr.strftime("%A, %B %d, %Y"))
# message = "GVR was born on {:%A, %B %d, %Y}."
# print(message.format(gvr))
#
# print(dir(datetime))
# launch_date = datetime.date(2017, 3, 30)
# launch_time = datetime.time(22, 27, 0)
# launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
# print(launch_date)
# print(launch_time)
# print(launch_datetime)
# print(launch_time.hour)
# print(launch_time.minute)
# print(launch_time.second)
#
# print(launch_datetime.year)
# print(launch_datetime.month)
# print(launch_datetime.day)
# print(launch_datetime.hour)
# print(launch_datetime.minute)
# print(launch_datetime.second)
#
# now = datetime.datetime.today()
# print(now)
# print(now.microsecond)
#
# moon_landing = "7/20/1969"
# moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
# print(moon_landing_datetime)
# print(type(moon_landing_datetime))

# collect string / test length

# str1 = input("Please enter a test string > ")
# if len(str1):
#     print("Your string is too short")
#     print("please enter a string with at least 6 characters")

# num = int(input("Enter a number > "))
# if num % 2 ==0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

# x, y, z = input("Enter length of 3 sides of a triangle > ").split()
# a = int(x)
# b = int(y)
# c = int(z)
# if a != b and b != c and c !=a:
#     print("this is an scalene triangle")
# elif a == b and b == c:
#     print("this is an equilateral triangle")
# else:
#     print("this is an isosceles triangle")

# functions ...
# print(dir())
#
# def f():
#     pass
#
#
# f()
# f
# print(f)
# print(dir())

# def ping():
#     return "Ping!"
#
#
# print(ping())
# x = ping()
# print(x)
# print(dir())

# import math
# print(dir(math))
# print(math.e)
# print(math.pi)
#
# def volmue(r):
#     """Returns the volume of a sphere with radius r""" # docstring..used for documentation
#     v = (4.0 / 3.0) * math.pi * r**3
#     return v
#
#
# print(volmue(2))
# print(help(volmue))
#
#
# def triangleArea(b, h):
#     """Returns the area of a triangle with base b and height h"""
#     return 0.5 * b * h
#
#
# print(triangleArea(3, 9))
# print(triangleArea(3, 6))
# print(help(triangleArea))
#

# keyword arguments
# 1 inch = 2.54 cm
# 1 foot 12 inches


# def cm(feet=0, inches=0):
#     """Converts a length from feet and inches to centimeters."""
#     inches_to_cm = inches * 2.54
#     feet_to_cm = feet * 12 * 2.54
#
#     return inches_to_cm + feet_to_cm
#
#
# print(cm(feet=5))
# print(cm(inches=5))
# print(cm(inches=70))
# print(cm(feet=5, inches=6))
# print(cm(inches=6, feet=5))
#
#
# def g(x, y=0):
#     return x + y
#
#
# print(g(5))
# print(g(12))
# print(g(5, y=6))

# sets
# example = set()
# print(dir(set))
# print(dir(example))
# help(example.add)
# example.add(42)
# example.add(False)
# example.add(2.718281828459045)
# example.add(3.141592653589793)
# example.add("Thorium")
# print(example)
# example.add(42)
# print(example)
# print(len(example))
# help(example.remove)
# example.remove(42)
# print(example)
# example.remove(50)
# print(example)
# help(example.discard)
# example.discard(50)
# print(example)
#
# example2 = set([28, True, 2.71828, "Helium"])
# print(example2)
# print(len(example2))
# example2.clear()
# print(example2)

# union and intersection of sets

# odd = {1, 3, 5, 7, 9}
# even = {2, 4, 6, 8, 10}
# prime = {2, 3, 5, 7}
# composite = {4, 6, 8, 9, 10}
#
# print(odd.union(even))
# print(even.union(odd))
# print(odd | even)
#
# print(odd.intersection(even))
# print(even.intersection(odd))
# print(odd & even)
#
# print(odd.intersection(prime))
# print(prime.intersection(odd))
# print(odd & prime)
#
# print(even.intersection(prime))
# print(prime.intersection(even))
# print(even & prime)
#
# print(prime.union(composite))
# print(composite.union(prime))
# print(prime | composite)
#
# print(2 in prime)
# print(6 in odd)
# print(9 not in even)
#
# print(composite.difference(even))
# print(composite - even)
#
# print(dir(prime))

# list

# example = list()
# example = []

# prime = [2, 3, 5, 7, 11, 13]
# print(prime)
# prime.append(17)
# prime.append(19)
# print(prime)
# print(prime[0])
# print(prime[1])
# print(prime[2])
# print(prime[-1])
# print(prime[-2])
# print(prime[-8])
#
# slicing
# print(prime[2:5])
# print(prime[0:6])
# print(prime[:4])
# print(prime[::-1])
# example = [128, True, "Alpha", 1.732, [64, False]]
# print(example[4])
# print(example[4][1])
#
# rolls = [4, 7, 2, 7, 12, 4, 7]
# print(rolls)
# rolls.reverse()
# print(rolls)
#
#
# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# print(numbers + letters)
# print(letters + numbers)
# print(dir(numbers))
# help(numbers.reverse)

# # dictionary

# post = {"user_id": 209, "message": "D5 E5 C5 C4 G4", "language": "English", "datetime": "20230215T124231Z", "location": (21.8121, 91.2384)}
# print(post)
# print(len(post))
# print(dir(post))
#
# print(post.keys())
# print(post.values())
# print(post.items())
#
# print(post["location"])
# print(post["message"])
# print(post["user_id"])
#
# print(type(post))
#
# post2 = dict(message="SS Cotopaxi", language="English")
# print(post2)
# post2["user_id"] = 208
# post2["datetime"] = "19771116T093001Z"
# print(post2)
#
# try:
#     print(post2["location"])
# except KeyError:
#     print("The post does not have a location")
#
# help(post.get)
# loc = post2.get("location", None)
# print(loc)
# pos = post.get("location", None)
# print(pos)
#
# print(post)
#
# for key in post.keys():
#     value = post[key]
#     print(key, "=", value)
#
# for key, value in post.items():
#     print(key, "=", value)
#
# post.pop("location")
# print(post)
# post.popitem()
# print(post)

# tuples
# import sys
# import timeit
# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# perfect_squares = (1, 4, 9, 16, 25, 36)
# print("# primes = ", len(prime_numbers))
# print("# squares = ", len(perfect_squares))
#
# for p in prime_numbers:
#     print("Prime: ", p)
# for n in perfect_squares:
#     print("Square: ", n)
#
# print("List methods")
# print(dir(prime_numbers))
# print(80*"-")
# print("Tuple methods")
# print(dir(perfect_squares))
# print(80*"-")
# print(dir(sys))
#
# help(sys.getsizeof)
#
# list_eg = [1, 2, 3, "a", "b", "c", True, 3.14149]
# tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14149)
#
# print("List size = ", sys.getsizeof(list_eg))
# print("Tuple size = ", sys.getsizeof(tuple_eg))
#
# list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=10000000)
# tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=10000000)
#
# print(list_test)
# print(tuple_test)
#
# empty_tuple = ()
# test1 = ("a")
# test2 = ("a", "b")
# test3 = ("a", "b", "c")
# print(empty_tuple)
# print(test1)  # returns just a string, not a tuple
# print(test2)
# print(test3)
#
# test4 = ("a",)  # returns a tuple, not a string
# print(test4)
#
# alternative construction of tuple
#
# t1 = 1,
# t2 = 1, 2
# t3 = 1, 2, 3
# print(t1)
# print(t2)
# print(t3)
#
# tuple with 1 element
# (age, country, knows_python)
#
# survey = (27, "Vietnam", True)
# age = survey[0]
# country = survey[1]
# knows_python = survey[2]
# print("Age =", age)
# print("Country = ", country)
# print("Knows Python?", knows_python)
#
# survey2 = (21, "Switzerland", False)
# age, country, knows_python = survey2
# print("Age =", age)
# print("Country = ", country)
# print("Knows Python?", knows_python)
#
# country = ("Australia") # returns string
# print(country)
# country = ("Australia",) # returns tuple of 1 element
# print(country)
#
# x, y, z = (1, 2, 3)
# print(f"({x}, {y}, {z})")

# # logging
#
#
#
#
#
# # logging

# recursion, fibonacci sequence and memoization
# without memoization
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for i in range(1, 101):
#     print(i, ":", fibonacci(i))
#     print(fibonacci(i), end=" ")

# with memoization
# explicit implementation of memoization

# fibonacci_cache = {}
#
#
# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     fibonacci_cache[n] = value
#       return value
#
#
# for n in range(1, 1001):
#     print(n, ":", fibonacci(n))


# with built in python tool(memoization)
# from functools import lru_cache
#
# @lru_cache(maxsize= 1000)
# def fibonacci(n):
#     if type(n) != int:
#         raise  TypeError("n must be positive integer")
#     if n < 1:
#         raise ValueError("n must be positive integer")
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for i in range(1, 501):
    # print(i, ":", fibonacci(i))
    # print(fibonacci(i), end=" ")
    # print(fibonacci(i+1)/fibonacci(i)) # golden ratio


# python random number generator
# the random moduel
import random
# print(dir(random))
# help(random.random)

# program to generate 10 random number from 0 up to 1(not including)
# generate random numbers in [0, 1)

# for i in range(10):
#     print(random.random())

# generate random numbers in [3, 7)

# def my_random():
#     # Random, scale, shift, return...
    # return 4*random.random() + 3
#
# for i in range(10):
#     print(my_random())


# # using uniform function(uniform distribution)
# help(random.uniform)
#
# for i in range(10):
#     print(random.uniform(3,7))


# # using uniform function(normal distribution)
# help(random.normalvariate)
#
# for i in range(10):
#     print(random.normalvariate(0, 1))

# for i in range(10):
#     print(random.normalvariate(4, 4))

# for i in range(10):
#     print(random.normalvariate(5, 0.01))

# for i in range(10):
#     print(random.normalvariate(5, 4))

# discrete probability distribution
# for i in range(10):
#     print(random.randint(1, 6), end=" ")

# li = [2, 3, 5, 7]
# for i in range(10):
#     print(random.choice(li), end=" ")

# outcomes = ["rock", "paper", "scissors"]
# for k in range(20):
#     print(random.choice(outcomes))

# working with csv file
#
#
#
#
#
#
# monti carlo simulation
#
#
#
#
#
#
#
# # list comprehension

# # ex-01 list of squares

# # without list comprehension, using for loop
# squares = list()
# for num in range(1, 101):
#     squares.append(num*num)
# print(squares)

# # using list comprehension
# squares2 = [x*x for x in range(1, 101)]
# print(squares2)

# # ex-02 list of remainders if square number is divided by 5

# remainder = [x**2 % 5 for x in range(1, 101)]
# print(remainder)

# remainder2 = [x**2 % 11 for x in range(1, 101)]
# print(remainder2)

# sub_list = []
# names = ["Adam", "Malar", "Vikram", "Vishnu", "Shiva", "Kartik", "Nayan", "Veda", "Vijay"]
# for name in names:
#     if name.startswith("V"):
#         sub_list.append(name)
#
# print(sub_list)
#
#
# li = [ name for name in names if name.startswith("V")]
# print(li)

# names = [("Adam", "Kerala"), ("Malar", "Kerala"), ("Vikram", "Tamil"), ("Vishnu", "Tamil"), ("Shiva", "Tamil"), ("Kartik", "Telegu"), ("Nayan", "Tamil"), ("Veda", "Tamil"), ("Vijay", "Tamil")]
#
# li = [name for (name, nationality) in names if nationality == "Tamil"]
# print(li)
# li = [name for (name, nationality) in names if nationality == "Kerala"]
# print(li)

# v = [2, -3, 1]
# print(4*v)

# v = [2, -3, 1]
# w = [4*x for x in v]
# print(w)

# A = [1, 3, 5]
# B = [2, 4, 7]
# C = [6, 8]
# cart = [(x, y) for x in A for y in B]
# print(cart)

# CLASSES AND OBJECTS
# OBJECT ORIENTED PROGRAMMING(OOP)

# class User:
#     pass
#
#
# user1 = User( ) #user1 is an instance i.e. object of User class
# user1.first_name = "Dave" #field..data attached to an object
# user1.last_name = "Bowman"
#
# print(user1.first_name)
# print(user1.last_name)
#
# first_name = "Arthur"
# last_name = "Clarke"
# print(first_name, last_name)
# print(user1.first_name, user1.last_name)
#
# user2 = User()
# user2.first_name = "Frank"
# user2.last_name = "Poole"
# print(user2.first_name, user2.last_name )
# user1.age = 37
# user2.favourie_movie = "Schindler's List"
# print(user1.age)
# print(type(user1.age))
# print(user2.favourie_movie)
# print(type(user2.favourie_movie))

# import datetime
#
# class User:
#     """A member of FriendFace. For now we are only
#         storing their name and birthday. But soon we
#         will store an uncomfortable amount of user
#         information in our database"""
#     def __init__(self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday
#
#         name_pieces = full_name.split(" ")
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#     def age(self):
#         """Returns the age of the user in years"""
#         today = datetime.date(2001, 5, 12)
#         yyyy = int(self.birthday[0:4])
#         mm = int(self.birthday[4:6])
#         dd = int(self.birthday[6:8])
#         dob = datetime.date(yyyy, mm, dd)
#         age_in_days = (today-dob).days
#         age_in_years = age_in_days / 365
#         return int(age_in_years)
#
# user1 = User("Zahidul Islam","19920924")
# print(user1.name)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.birthday)
# print(user1.age())
# help(User)


# python and prime numbers

import time
import math

# # version 1
# def is_prime_v1(n):
#     """Return 'True' if 'n' is a prime number. False otherwise"""
#
#     if n == 1:
#         return False
#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     return True
#
#
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v1(n)
#     print(n, is_prime_v1(n))
# t1 = time.time()
# print(f"Time required: {t1-t0}")
#
#
#
# # version 2
# def is_prime_v1(n):
#     """Return 'True' if 'n' is a prime number. False otherwise"""
#     max_divisor = math.floor(math.sqrt(n))
#     if n == 1:
#         return False
#     for d in range(2, 1 + max_divisor):
#         if n % d == 0:
#             return False
#     return True
#
#
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v1(n)
    # print(n, is_prime_v1(n))
# t1 = time.time()
# print(f"Time required: {t1-t0}")


# # version 3
# # skipping all the odds
# def is_prime_v1(n):
#     """Return 'True' if 'n' is a prime number. False otherwise"""
#
#     if n == 1:
#         return False
#     if n == 2:
#         return True
#     if n > 2 and n % 2 == 0:
#         return False
#
#     max_divisor = math.floor(math.sqrt(n))
#     for d in range(3, 1 + max_divisor, 2):
#         if n % d == 0:
#             return False
#     return True
#
#
# t0 = time.time()
# for n in range(1, 100000):
#     is_prime_v1(n)
    # print(n, is_prime_v1(n))
# t1 = time.time()
# print(f"Time required: {t1-t0}")

# # JOSN(Java Script Object Notation)

#
#
#
#
#
#
#
#
#
#
# # Lambda Expression and anonymous function

# write a function to compute 3x+1

# def f(x):
#     return 3*x + 1
#
#
# print(f(2))
#
# g = lambda x: 3*x + 1
# print(g(3))

# # combining first name and last name to make full name
# full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
#
# first_name = "Zahidul"
# last_name = "jewel"
# print(full_name(first_name, last_name))


# sorting by last name from a list of names
# authors = ["Isaac Asimov", "Douglas Adams", "Arthur C. Clarke", "H. G. Wells", "Khushbant Singh"]
# print(authors)
# help(authors.sort)
# authors.sort(key=lambda name: name.split(" ")[-1].lower())
# print(authors)

# def build_quadratic_function(a, b, c):
#     """Returns the function f(x) = ax^2 + bx + c"""
#
#     return lambda x: a*x**2 + b*x + c
#
# f = build_quadratic_function(1, -5, 6)
# print(f(0))
# print(f(1))
# print(f(2))
# print(build_quadratic_function(4, 0, 6)(2))



# map, filter and reduce function
# map()
# filter()
# reduce()

# import math
#
# def area(r):
#     """Area of a cricle with radius 'r'."""
#     return math.pi*(r**2)
#
#  print(area(5))
#
# radii = [2, 5, 7.1, 0.3, 10]
#
# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)
#
#
# print(areas)
#
# with map
# print(map(area, radii)) # map object
# print(list(map(area, radii)))


# # degree to farehnite from a list of temperature
# temps = [("Berlin", 29), ("Bonn", 23), ("Cairo", 39), ("Buenos Aires", 22), ("Berijing", 29), ("Berlin", 24), ("London", 19)]
#
# c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
# li = list(map(c_to_f, temps))
# print(li)

# # filter()
import statistics
# data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# print(data)
# avg = statistics.mean(data)
# print(avg)
# li = list(filter(lambda x: x > avg, data))
# print(li)
#
# li2 = list(filter(lambda x: x < avg, data))
# print(li2)
#
# latin_america = ["", "Argentina", "Brazil", "", "Chile", "Columbia", "Uruguay", "", "", "Ecuador", "Venezuela"]
# li3 = list(filter(None, latin_america))
# print(li3)

# reduce
# from functools import reduce
# multiply all numbers in a list
# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# multiplier = lambda x, y: x*y
# print(reduce(multiplier, data))

# using for loop
# product = 1
# for x in data:
#     product = product * x

# print(product)

# sorting in python
# earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]# earth_metals.sort()
# print(earth_metals)
# earth_metals.sort(reverse=True)
# print(earth_metals)
# help(list.sort)
#
# 8 planetesinfo
# format := (name, radius, density, distance from sun)
#
# planets = [
#     ("Mercury", 2440, 5.43, 0.395),
#     ("Venus", 6052, 5.24, 0.723),
#     ("Earth", 6378, 5.52, 1.000),
#     ("Mars", 3396, 3.93, 1.530),
#     ("Jupiter", 60268, 1.33, 5.210),
#     ("Saturn", 60268, 0.69, 9.551),
#     ("Uranus", 2559, 1.27, 19.213),
#     ("Neptune", 24764, 1.64, 30.070)
# ]
#
# size = lambda planet: planet[1]
# planets.sort(key=size, reverse=True)
# print(planets)
#
# alphabetic = lambda planet: planet[0]
# planets.sort(key=alphabetic)
# print(planets)
#
# density = lambda planet: planet[2]
# planets.sort(key=density, reverse=True)
# print(planets)

# earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
# print(sorted(earth_metals))
# print(earth_metals)
#
# data = (4, 9, 2, 3, 5, 7, 8, 1, 6)
# print(data)
# li = sorted(data)
# print(li)
# print(data)
# str1 = "Alphabetical"
# lst1 = sorted(str1)
# print(lst1)




# text file in python
# help(open)
# reading a file
# read()

# fhand = open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\gollum.txt", "r")
# lines = fhand.read()
# print(lines)

# f = open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\clown.txt")
# text = f.read()
# f.close()
# print(text)


# safer way to open a file
# with open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\clown.txt") as f:
#     text = f.read()
# print(text)

# try:
#     with open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\bilbo.txt") as b:
#         text = b.read()
# except FileNotFoundError:
#     text = None
# print(text)

# writing to a file

# oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
# continents = ["Asia", "Europe", "Africa", "North America", "South America", "Australia", "Antarctica"]

# with open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\earth_info.txt", "w") as earth:
#     for ocean in oceans:
#         print(ocean, file=earth)
#         # earth.write(ocean)
#         # earth.write("\n" )


# with open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\earth_info.txt") as f:
#     text = f.read()
# print(text)

# with open("C:\\Users\\Jewel81\\Desktop\PYTHON\\textfiles\\earth_info.txt", "a") as g:
#     # text = g.read()
#     print(23*"=", file=g)
#     print("There are 7 continents.", file=g)
#     for continent in continents:
#         # print(continent, file=g)
#         g.write(continent)
#         g.write("\n")

# # unittest in python
#
#
#
#
#
#
#
# Exception in python

# for i in range(5):
#     print("Hello, World")

# print(1/0)

# with open("x_files.txt") as xf:
#     the_truth = xf.read()
#
# print(the_truth)

# print(1 + 2 + "three")

# from math import sqrt
# print(sqrt(-1))

# from cmath import sqrt
# print(sqrt(-1))

# li = [4, 9, 2, 3, 5, 7]
# for i in range(10):
#     print(li[i])

# di = {1: "Kamal", 2: "Adam", 4: "Nasir"}
# print(di[2])
# print(di[3])

# Objective
# write a function that reads binary file and return data
# mesure time required

# logging example
#
#
#
#
#
#
#
# # urllib
# # GET Requests
# import urllib

# ex-01
# from urllib import request
# print(dir(request))
# resp = request.urlopen("https://www.wikipedia.org")
# print(type(resp))
# print(dir(resp))
# print(resp.code)
# print(resp.length)
# print(resp.peek())
# data = resp.read()
# print(type(data))
# print(len(data))
# html = data.decode("UTF-8")
# print(type(html))
# print(html)
# print(resp.read())
#
# # ex-02
# resp = request.urlopen("https://www.google.com/search?client=firefox-b-d&q=python+raise+exception")
# print(type(resp))
# print(resp.isclosed())