# # 001 install and setup for mac and windows
# print("Hello World")

# # 002 strings - working with textual data
# message = "Hello world"
# print(message)
#
# message2 = "Boby's World"
# print(message2)
#
# message3 = 'Sophie\'s World'
# print(message3)
#
# message4 = """ Boby's was was a good cartoo
# earlier in 1990s. but now it is gone. """
# print(message4)
#
# print(len(message))
# print(len(message2))
# print(len(message3))
# print(len(message4))
#
# # slicing
# print(message[0])
# print(message[10])
# print(message[0:5])
# print(message[0:5])
# print(message[:5])
# print(message[6:])
#
# # string operations
# print(message.lower())
# print(message.upper())
# print(message.count("l"))
# print(message.count("Hello"))
# print(message.find("world"))
# print(message.find("universe"))
# new_message = message.replace("world", "universe")
# print(message)
# print(new_message)
# message = message.replace("world", "universe")
# print(message)
#
# #concatenation
# greeting = "Hello"
# name = "Michael"
# message5 = greeting + ", " + name + ". Welcome!"
# print(message5)
#
# #formatted string
# message6 = "{}, {}. Welcome!".format(greeting, name)
# print(message6)
#
# #f' string
# message7 = f"{greeting}, {name}. Welcome!"
# print(message7)
# message8 = f"{greeting}, {name.upper()}. Welcome!"
# print(message8)
#
# print(dir(message))
# print(help(str))
# print(help(str.lower))


# # 003 integers and floats - working with numeric data
#
# num = 3
# print(type(num))
# num = 3.141592653589793
# print(type(num))
# # arithmetic operators
# a = 3
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
# print(a ** b)
# # oder of operation i.e. operator precedence
# print(3 * 2 + 1)
# print(3 * (2 + 1))
# num = 1
# num = num + 1
# print(num)
# num += 1
# print(num)
# num -= 1
# print(num)
# num *= 2
# print(num)
# num -= 2
# print(num)
# # builtin functions
# print(abs(-3))
# print(round(3.75))
# print(round(3.141592653589793, 4))
# print(round(2.7118281828459045, 3))
# # comparision operators
# a = 3
# b = 2
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# var1 = '1971'
# var2 = '2019'
# var = var1 + var2
# print(var)
#
# var1 = '1971'
# var2 = '2019'
# var1 = int(var1)
# var2 = int(var2)
# # var = int(var1) + int(var2)
# var = var1 + var2
# print(var)
# # alt. using eval() function
# var1 = '1971'
# var2 = '2019'
# var = eval(var1) + eval(var2)
# print(var)

# # Lists, Tuples amd Sets
# # lists
# # ordered
# # mutable
# # list operations

# courses = ["Python", "C++", "Java", "Data Structures", "Algorithms"]
# # slicing
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[4])
# print(courses[-1])
# print(courses[0:5])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])
# print(courses[2:])
# courses.append("SQL")
# print(courses)
# courses.insert(0, "Networking")
# print(courses)
# new_course = ["DLD", "TOC", "Math", "EEE"]
# # courses.insert(0, new_course)
# # print(courses)
# courses.extend(new_course)
# print(courses)
# courses.remove("Math")
# print(courses)
# courses.pop()
# print(courses)
# catch = courses.pop()  # important
# print(catch)
# print(courses)
# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
# courses.sort(reverse=True)
# print(courses)
# nums = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# li = sorted(nums)  # returns a copy
# print(li)
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(courses.index("C++"))
# print(courses)
# print("Java" in courses)
# print("Math" in courses)
# print("C++" not in courses)
# for item in courses:
#     print(item)
#
# for index, course in enumerate(courses):
#     print(index, course)
#
# for index, course in enumerate(courses, start=1):
#     print(index, course)
# course_string = ', '.join(courses)
# print(course_string)
#
# course_string = ' - '.join(courses)
# print(course_string)
#
# new_list = course_string.split(" - ")
# print(new_list)

# # tuples
# # tuples are immutable
# # ordered

# li = [4, 9, 2, 3, 5, 7]
# nums = (4, 9, 2, 3, 5, 7, 8, 1, 6)
# courses = ('SQL', 'Python', 'Networking', 'Java', 'Data Structures', 'DLD', 'C++', 'Algorithms')
# subjects = courses
# print(courses)
# print(subjects)
# print(nums.index(5))
# print(courses.index("C++"))
# print(courses.count("Java"))
# t = tuple(li)
# print(li)
# print(t)

# # sets
# # mutable
# # unordered
# # non-duplicate members
#
# # set operations
# cs_courses = {'SQL', 'Python', 'Networking', 'Java', 'Data Structures', 'DLD', 'C++', 'Algorithms', 'C', 'Java', 'Python'}
# print(cs_courses)
# print("SQL" in cs_courses)
# print("Math" in cs_courses)
# A = {1, 3, 5, 7, 9}
# B = {2, 3, 5, 7}
# print(A.union(B))
# print(A | B)
# print(A.intersection(B))
# print(A & B)
# print(A.difference(B))
# print(A - B)
# print(B.difference(A))
# print(B - A)
#
# # empty list, tuples, sets
# li = []
# list1 = list()
# t = ()
# t1 = tuple()
# s = set()


# # 005 dictionaries
# # similar to hash map
# # and associative array
#
# # dictionary operation
#
# student = {"name": "Jewel", "age": 28, "courses": ["C++", "Java", "Python"]}
# print(student)
# print(student["name"])
# print(student["courses"])
# print(student["courses"][2])
# # print(student["contact"])
# print(student.get("name"))
# print(student.get("contact"))
# print(student.get("nationality", "Not Found"))
# student["contact"] = "01729323232"
# print(student)
# print(student.get("contact"))
# student["name"] = "Zahid"
# print(student)
# student.update({"name": "Robi", "age": 26, "contact": "01515215353"})
# print(student)
# del student["age"]
# print(student)
# phone = student.pop("contact")
# print(phone)
# print(student)
#
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())
#
# for key in student:
#     print(key)
#
# for key, value in student.items():
#     print(key, value)


#  006 conditionals and booleans
#  if, else and elif statements
# if True:
#     print("Conditional was True")
# if False:
#     print("Conditional was False")

# language = "Python"
# if language == "Python":
#     print("Conditional was True")
#
# # language = "Python"
# language = "C++"
# if language == "Python":
#     print("language is python")
# else:
#     print("language is not python")

# language = "C++"
# if language == "Python":
#     print("language is python")
# elif language == "C++":
#     print("language is C++")
# else:
#     print("No Match")

# boolean operations
# and
# or
# not

# # and example
# user = "Admin"
# # logged_in = True
# logged_in = False
# if user == "Admin" and logged_in == True:
#     print("Admin Page.")
# else:
#     print("Bad Creds")

# # or example
# user = "Admin"
# # logged_in = True
# logged_in = False
# if user == "Admin" or logged_in == True:
#     print("Admin Page.")
# else:
#     print("Bad Creds")

# # not example
# logged_in = False
# if not logged_in:
#     print("Please Log In.")
# else:
#     print("Welcome.")

# A = [1, 2, 3]
# B = [1, 2, 3]
# print(A)
# print(B)
# print(A == B)  # values are same so equal(==)
# print(A is B)  # memory locations are different
# print(id(A) == id(B))
# print(id(A) != id(B))
# print(id(A))
# print(id(B))
#
# C = A
# print(A)
# print(C)
# print(id(A))
# print(id(C))
# print(id(A) == id(C))
# print(id(A) != id(C))
# print(A == C)
# print(A is C)
#
# # true and false evaluation test
# condition = False
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = None
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = 0
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = 10
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = []
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = ""
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = {}
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = ()
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# condition = "Test"
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")


# 007 loops and iterations
# for while loops
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(num, end=" ")

# #break
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print("Found")
#         break
#     print(num, end=" ")

# # continue
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print("Ignored!")
#         continue
#     print(num, end=" ")

# # continue
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print("Passed!")
#         pass
#     print(num, end=" ")

# # loop within a loop
# # nested loop
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     for letter in "abc":
#         print((num, letter))

# # range function
# for i in range(10):
#     print(i, end=" ")

# for i in range(1, 11):
#     print(i, end=" ")

# for i in range(1, 11, 2):
#     print(i, end=" ")

# # while loop
# x = 0
# while x < 10:
#     print(x, end=" ")
#     x += 1

# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x, end=" ")
#     x += 1

# x = 0
# while True:
#     if x == 5:
#         break
#     print(x, end=" ")
#     x += 1

# # infinite loop
# x = 0
# while True:
#     print(x)
#     x += 1


# # 008 Functions
# def hello_func():
#     # pass
#     print("Hello world.")
#
# # print(hello_func)  # returns function object
# hello_func()

# def hello_func():
#     return "Hello world."
#
# s = hello_func()
# print(s)

# print(len("Test"))

# def hello_func():
#     return "Hello world."
#
# s = hello_func().upper()
# print(s)

# # argument passing in function parameters
# def greet(message):
#     return "{} Function".format(message)
#
# s = greet("Hello")
# print(s)

# # default parameters
# def greet(message, name="You"):
#     return "{}, {} Function".format(message, name)
#
# # s = greet("Hello", "Zahid")
# s = greet("Hello", name="Zahid")
# t = greet("Hi")
# print(s)
# print(t)

# def student_info(*args, **kwargs): # allows to accept arbitrary number of...
#     # position and keyword arguments
#     print(args)  # positional arguments
#     print(kwargs)  # keyword arguments
#
# student_info("Math", "EEE", name="Zahid", age=28)

# # unpacking number of arguments in function call
# def student_info(*args, **kwargs): # allows to accept arbitrary number of...
#     # position and keyword arguments
#     print(args)  # positional arguments
#     print(kwargs)  # keyword arguments
#
# courses = ["Python", "C++", "Java", "DS", "Algo", "DLD"]
# info = {'name': 'Zahid', 'age': 28}
# student_info(*courses, **info)  # unpacking lists and dictionary...
# # and passing them individually to the function parameters


# # Example from python documentation
# # a function checks leaps year..returns true or false
# # another function returns number of days in the month
#
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def is_leap(year):
#     """Return True for leap years and False for non-leap years."""
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
#
#
# def days_in_month(year, month):
#     """Return number of days in that month in that year."""
#     if not 1 <= month <= 12:
#         return "Invalid Month"
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]
#
#
# print(is_leap(2019))
# print(is_leap(2020))
# print(days_in_month(2020, 2))
# print(days_in_month(2019, 2))
# print(days_in_month(2000, 4))


# 009 import modules and exploring the standard library
# creating modules
# how does modules work
# python packages and library

# import my_module
# courses = ["Python", "C++", "Java", "DS", "EEE", "DLD"]
# index = my_module.find_index(courses, "DLD")
# print(index)

# import my_module as mm
# nums = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# pos = mm.find_index(nums, 1)
# print(pos)
# print(mm.test)


# from my_module import find_index as fi
# # importing this way just restricts to particular function
# li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# position = fi(li, 6)
# print(position)


# from my_module import find_index, test
# P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# i = find_index(P, 19)
# print(i)
# print(test)


# from my_module import *
# P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# i = find_index(P, 10)
# print(i)

# # import sys
# # print(sys.path)
#
# import random
# import math
# import datetime
# import calendar
# import os
# import webbrowser
# import antigravity
#
# courses = ["Python", "C++", "Java", "DS", "EEE", "DLD"]
# P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# nums = [4, 9, 2, 3, 5, 7, 8, 1, 6]
#
# random_course = random.choice(courses)
# print(random_course)
#
# rads = math.radians(90)
# print(rads)
# ratio = math.sin(math.pi*.333)
# print(ratio)
#
# today = datetime.date.today()
# print(today)
#
# is_leap = calendar.isleap(2018)
# print(is_leap)
#
# print(os.getcwd())
# print(os.__file__)
#
# webbrowser.open("https://xkcd.com/353/")
# # webbrowser.open("https://www.wikipedia.org")


