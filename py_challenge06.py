'''7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''
#solution
file = open(input('enter file name: '))
#string to be found
identifier = 'X-DSPAM-Confidence: '
#place to store all found numbers
all_nos = ''
#serching through file for line with identifier
for i in file:
    if i.startswith(identifier):
        all_nos += i[identifier.index(identifier[-1]):-1]
#I know there is sum() & len() function, but I wanna do it with loops, so add for sum and count for no 
count = 0       
add = 0
for p in all_nos.split():
    add = add + float(p)
    count += 1
print(add / count)
