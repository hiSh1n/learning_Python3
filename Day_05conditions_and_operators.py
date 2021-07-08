#conditions
#printing output depending on the conditions
#note: out only print if atleast one condition should be satisfied
''' 
if it's hot(if condition)
    it's a hot day
    drink plenty of water
otherwise if it's cold (elif condition)
    it's cold day
    wear warn clothes
otherwise(else condition)
    it's a lovely day
'''
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")

print("enjoy your day")

#simple down payment
'''
price of a house is $1M
if buyer has good credit,
they need to put down 10%
otherwise
they need to put down 20%
print the down payment
'''
house_price = 1000000
good_credit = False
if good_credit:
    print("congraltulations!")
    print("$" + str(house_price * 0.1) + " is your down payment!")
else:
    print("congraltulations!")
    print("$" + str(house_price * 0.2) + " is your down payment!")
'''
better solution
house_price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    print(f"Down Payment: ${down_payment}")
'''
#logical operators
# and operator, bot conditions shoud be true
# or operator, atleast one condition should be true
#not operator converts true to flase and vice versa.
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("you are eligible for loan")

#conparasion operators
'''
'=' this is assignment operator, it assigns values
'==' this is equality operator, it means equality
'<' less than
'>' greater than
'<=' less than or equal to
'>=' greater than or equal to
'!=' not equal
'''
#challenge make a validation form with character restriction
name = input("Enter your name ")
char_count = len(name)
if char_count < 3:
    too_small = True
    print('name must be atleast 3 chars long')
elif char_count > 25:
    too_big = True
    print("name too long !")
else:  
    print("nice name :)")

