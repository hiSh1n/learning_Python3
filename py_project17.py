#To count the total, highest and lowest possible values given the no. of bits in binary.
bitno = int(input("Enter no. of bits:  "))
storage = [1,]
i = 1
while len(storage) < bitno:
    i = i * 2
    storage.append(i)
print(storage)
print('Total possible values: ', sum(storage) + 1)
print('Highest possible value: ', sum(storage))
print('Lowest possible value: ', 0)
