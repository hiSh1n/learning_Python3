import math
#This is day 04
#ARITHMETIC OPERATORS
#we have two types of numbers in python whole no.'s and floats(decimal)
#addition

print(3 + 4)

#subtraction

print(9 - 5)

#multiplication

print(4 * 5)

#Division

#Dfor float
print(10 / 3)

#Dfor int
print(10 // 3)

#modulus (returnes remainder of division)

print(10 % 3)

#exponent

print(10 ** 3)

#augemented assignment operator, used to do arithemitic but in more readable/shorter form.
#for example
x = 5
x = x + 3
#we can write (x = x + 3) as (x += 3)
print(x)

y = 5
y += 3
print(y)

#BEDMAS is applied in arithemetic python
#bracket>exponentiation>division>multiplication>addition>subtraction
x = (1 + 2) * 50 * 2 / 1 + 5 - 2
print(x)

#math functions
#round() always returns rounded value
x = 0.7
print(round(x))

#abs() absolute, always returns +ve values of any input even -ve no.'s
x = -76
print(abs(x))

#MODULES
#import math (look at first line)
#we can access module functions using the .(dot) operator.
#.ceil return the ceiling value of a number
#there are many function so can learn them online when need
print(math.ceil(9.1))

