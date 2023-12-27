def pnumber(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True
i=0 
sumpnumber = 0
while i < 2000000 :
    if pnumber(i):
        sumpnumber = sumpnumber + i 
    i += 1 
print(sumpnumber)