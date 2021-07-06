#program to calculate BMI(Body mass index)
weight = float(input("enter weight "))
height = float(input("enter height "))
result = weight/height**2
if result < 18.5:
     print("Underweight")
elif result >= 18.5 and result<25:
     print("Normal")
elif result >= 25 and result<30:
    print("Overweight")
elif result > 30 :
    print("Obesity")
