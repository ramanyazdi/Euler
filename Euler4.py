def revnumber(n):
    txt = str(n)
    if txt == txt[::-1]:
        return True
    else:
        return False 

# solution 1: 
palindromic = [] 
for i1 in range(100,1000):
    for i2 in range(100,1000):
        answer = i1 * i2
        if revnumber(answer):
            palindromic.append(answer)
print(max(palindromic))

# solution 2: 
palindromic = 0
for i1 in range(100,1000):
    for i2 in range(100,1000):
        answer = i1 * i2
        if revnumber(answer) and answer > palindromic:
            palindromic = answer 
print(palindromic)
