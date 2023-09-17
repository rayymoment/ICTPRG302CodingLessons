# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

# Keywords (Cannot use these within variables)
import keyword
print (keyword.kwlist)

# Python Built-In Functions
print ("Hello World")
print ("Hello, what is happening?")
z = ("pie", "cake", "sausage roll")
print(z)

print ("Hello", "how are you?", sep=" ---")

# Determining a Variable
x = "Rayyan"
print (x)

# Calculating the user's Age given their date of birth
from datetime import datetime
Year = int(input("Please enter the year you were born: "))
Month = int(input("Please imput the number of the month you were born. (For example 8 = August: "))
Day = int(input("Please enter the day you were born: "))

DateOfBirth = datetime(Year, Month, Day)
Age = datetime.now() - DateOfBirth
print("You are " + str(Age.days) + " days old")

convertdays = int(Age.days)
AgeYears = convertdays/365

print("Or " +str(AgeYears) + " years old to be less precise")
print(type(AgeYears))

# Creating a variable and using the assignment operator
NoOfItems = 5
print (NoOfItems)
# Adding another item
NoOfItems = NoOfItems + 1
print (NoOfItems)
# Reassigning a string type to NoOfItems
NoOfItems = "Six"
print(NoOfItems)

#Adds two numbers together (NOT addition)
num1=input("Enter a number between 1 and 100: ")
num2=input("Enter another number between 1 and 100: ")

print ("Number 1 + Number 2=", num1+num2)
