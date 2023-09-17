# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

#Excercise 1
a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("b is not greater than a")

#Excercise 2
x = 1
if (x > 0):
    a = 0
    b = 1
print(a,b)

#Excercise 3
print(5 > 4)
print(10 == 10)
i = 42
print(i > 10)
j = 17
print (j <= 1)

#Excercise 4
i = 42
j = 17

if j <= i:
    print("j is less than or equal to i")

#Excercise 5
subjectFinalMark=int(input("Please enter the student's subject final mark: "))

if (subjectFinalMark >= 0 and subjectFinalMark < 50):
    print("The student's final grade is FAIL!")
elif (subjectFinalMark >= 50 and subjectFinalMark < 60):
    print("The student's final grade is PASS!")
elif (subjectFinalMark >= 60 and subjectFinalMark < 75):
    print("The student's final grade is CREDIT!")
elif (subjectFinalMark >= 65 and subjectFinalMark < 85):
    print ("The student's final grade is DISTINCTION!")
elif (subjectFinalMark >= 85 and subjectFinalMark < 100):
    print("The student's final grade is HIGH DISTINCTION!")
else:
    print("Please enter values from 0 to 100.")





