#This is day 2

#some variable converters int(),str(), bool(), input(), type(), print(), float(), by default everything is string.

#Exercise 03-
#age finder

birth_year = input("what's your Birth Year:")
age = (2021 - int(birth_year))
print("your are " + str( age) + " years old !")

print("             ")
#Exercise 04-
#pound to kilo weight convertor-

your_weight = input("Enter the weight in pounds: ")
a_kilo = (int(your_weight) / 2.20)
print(str(your_weight) + ' Pound is equal to ' + str(a_kilo) + " kg")

print("             ")
#python indexing
#python indexes strints like 'APPLE'
#                             01234
#there's also negitive indexing line 'A P P L E'
#                                       ...-2 -1 
#index printing

dummy = 'jojo'
print(dummy[0])
#output = j, 0

print(dummy[0:3])
#output = joj, 0,1,2
print("             ")

#formatted strings, use f'{placeholder for variable} no concatenation needed.
first_name = 'jonny'
last_name = 'jake'
message = f'{first_name} {[last_name]} is our secret agent! '
#without f'string I have to write it as
#message = first_name + ' [' + last_name + ' ]' + 'is our secret agent!'
print(message)

print("             ")
#TO BE CONTINUE...
