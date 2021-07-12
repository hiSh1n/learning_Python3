#write a program in python that will calculate fibonacci series.
a = 0
b = 1
i = a
while True:
  if i == a or b and i < 1:print(i) 
  i = a+b
  print(i)
  a = b
  b = i
#increase or decrease or remove this last line according to the numbers you want.
  if i > 50:break
