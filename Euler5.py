# simple solution 
def noreminder(n):
    for i in range(1,21):
        if n%i==0:
            continue
        else:
            return False

n =1
while noreminder(n) == False:
    n += 1
else:
    print(n)

# professional solution 
import math

def find_smallest_multiple():
    return math.lcm(*range(1, 21))

result = find_smallest_multiple()
print(result)

