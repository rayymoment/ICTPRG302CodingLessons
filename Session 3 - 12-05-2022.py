#Example 1
x = 42 # is of type int
y = "Rayyan" # y is type of string
print(x)
print(y)

#Example 2
x = 42 # x is of type int
print(x)
x = "Arthur" # x is now type of string
print(x)

#Example 3
theMeaningOfTheUniverse = 123456789 # this variable is a bit long but good to read.
print(theMeaningOfTheUniverse)

#Example 4 - Variable intended to cause error (originally "2ndBirdType" Cannot be variable at the start. Replaced with underscore.
_2ndBirdType = "African Swallow"
print(_2ndBirdType)

#Example 5 - Creating variables to combine - concatenate
birdtype1 = "African Swallow" # This variable contains a string.
print("How fast can an unladen " + birdtype1 + " fly?")

#Example 6 - Converting interger variable to string
birdtype1 = "African Swallow" # This variable contains a string value
_indicatedAirSpeed = 12 # This variable contains an interger value.
print("The indicated air speed of an "+ birdtype1 + " is " + str(_indicatedAirSpeed) + " knots.")

#Example 7 - Running code and reviewing the result
print(3+2)
print(320+12553212)
print(3-2)
print(3*2)
print(55/3)
print(55%3)
print(3**3)
print(5//2)
print(5//3)
print((5+7) * (22-3) * (3/9))

#Example 8 - Determining if a users mathematical imput is even or odd.
usersNumber = int(input("Please enter a number "))
if (usersNumber % 2) == 0:
    print("Thanks! Your number is even.")
else:
    print("Thanks! Your number is odd.")

#Example 9 - Exploring Comparison Operators
x=5
y=9

#Check if y is greater than x
print("x > is ", x > y)

#Check if y is less than x
print("x < y is ", x <y)

#Now check if x and y are equal
print("x == y is ", x == y)

#Check if x and y are not equal
print("x != y is ", x != y)

#Check if x is greater than or equal to y
print("x >= y is ", x >= y)

#Check if x is less than or equal to y
print("x <= y is ", x <= y)