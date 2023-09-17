# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

import math
a = -42
math.fabs(a)
print (a)


import math

# The .fabs() function of the math library returns the absolute value of a number.
print(math.fabs(-345))

import random
for i in range(10):
    print(random.randint(1, 25))

from math import sqrt
print("Welcome to the Hypotenuse calculator!")

sideA = float(input("Please enter the lengh of side 'a': "))
sideB = float(input("Please enter the length of side 'b': "))

c = sqrt(sideA ** 2 + sideB ** 2)
print("Thank you! The length of the Hypotenuse is ", str(c))

from datetime import date
theDate = date(2019, 2, 24)
print("The date is: ", theDate)

#Passing named arguments out of order
theDate = date(day = 24, month = 2, year = 2019)
print("The date is: ", theDate)

from datetime import time
theTime = time(22, 46, 15, 200)
print("The time is ", theTime)

# Creating a date object with the value of 01/02/1961
dateofBirth = date(year=1961,month=2,day=1)

print("Your date of birth is ", dateofBirth)
yr = dateofBirth.year
mth = dateofBirth.month
dy = dateofBirth.day
print("You were born on the ", dy, "day of the ", mth, "month in the year", yr)


# returning the current date using the .today() function
todaysDate = date.today()
print("Today's date ", todaysDate)

movieName = "The Life of Brian"
print(movieName[-1])

