import math
def uoc(n):
    dem = 0
    for i in range(2, round((n/2)+1)):
        if (n%i == 0):
            if (i%2 == 1): dem += 1
            if ((n%(n/i)%2) == 1): dem += 1
    return dem
    
n = int(input())
print(uoc(n))