
# Solution 1
list1 =[]
list2 = []

for i in range(1,101):
    x = i ** 2
    list1.append(x)
    list2.append(i)

print(sum(list1))
print(sum(list2)**2)
print(sum(list2)**2 - sum(list1))

# Solution 2
sumOfSq = sum(i**2 for i in range (1,101))
SqOfSum = (sum(i for i in range(1,101)))**2
print(sumOfSq)
print(SqOfSum)
print(SqOfSum - sumOfSq)





