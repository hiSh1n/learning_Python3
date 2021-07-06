#To calculate simple and compound interest of  2 years.

P = int(input("Enter principle amount: "))
R = float(input("Enter rate: "))
T = 2

si = P * R * T / 100

print("Your simple interest for 2 years is ", si)

A = round(P * (1+R/100)**2, 2)
print("Your conpound interest for 2 years is ", A - P)
