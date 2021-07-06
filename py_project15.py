#Python programs to find the sum of consecutive numbers.

#1st method
#asking for first no.
inp = int(input('first number: '))
sum = 0
#asking for last no.
la = int(input('last number: '))
#addking all consecutive numbers from first to last. e.g. inp=5 & la=10, so the sum will be 5+6+7+8+9+10
for i in range(inp,la+1):
    sum = sum+i
print(sum)

#2nd method

#just taking last number and outputing the sum of consecutive from 0-last number.e.g. N=5, sum will be 1+2+3+4+5
N = int(input())
sum = 0
for i in range(N+1):
    sum += i
print(sum)
