
def primeNum(n):
    if n<=1: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True 

n = 1 
pnposition = 0
while pnposition < 10001:
    if primeNum(n): 
        pnposition += 1
        n += 1
    else:
        n += 1

print(n-1)

