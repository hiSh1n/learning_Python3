#This is Day 1
#I am learning Python
#I'll add more comments as I'll learn more things
#NOTE_FOR_FUTURE_ME: "Don't you dare drop off in the middle"

#first line of code-

print("Hello! World")

#how python got executed.
#the python intrepreter executes code line by line.


print("             ")
#Drawing Dog with Python-

print('Look here, a dog')
print('0------/')
print('  |\ |\ ')

print("              ")
#code below first print our value inside '' then perform the operation i.e; * 10

print('*' * 10)

print("             ")
#variables-
#used to tempreraly store data

example_variable = 'Iam a variable'
print(example_variable)

#types of var no.s
#integers are whole no.'s 0-100000...
#float are decimal no.'s -10000... - + 100000... , -5,etc
#string are literal values "this is a string"
#boolean = either True or False
print("             ")
#keep in mind-
#Python is case sensitive meaning Flag and flag have different meaning
#you should always use lower case when definig variables, 
#Python keywords are reserved values which have special meaning, do not use any keyword name as var name.

#exercise01-
#write a program for hospital to check on patients staus
#we check in a patient named John Smith.
#He's 20 years old and is a new patient.
#task
#define 3 vars to define his name,age and status(new/existing)
#My_Solution01-

patient_Name = "John Smith"
Patient_Age = 20

#Here I used patient_record = "New" but should have used booleam is_new = true

is_new = True
print(patient_Name)
print(Patient_Age , "years")
print('is new?', is_new )

print("             ")
#recieving input from user
#Here input is taking input form user and storing it in var name

name = input("what's your name? ")
print('hi, ' + name)

print("             ")
#exercise02
#task
#ask two questions, name and fav color, then print message name likes fav color

name = input("what's your name? ")
fav_color = input("what's your fav color? ")
print(name + " likes " + fav_color)

print("             ")
#I think that's enough for today, to be continued...