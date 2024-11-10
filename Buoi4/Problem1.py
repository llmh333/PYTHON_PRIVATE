k = int(input("K = "))
a = [int(input()) for _ in range(k)]

n = int(input("N = "))
m = int(input("M = "))


dem = 0
b = []
temp = []
if (n*m <= k):
    for i in range(n*m):
        temp.append(a[i])
        dem += 1
        if (dem == n):
            b.append(temp)
            temp = []
            dem = 0
    print(b)
    
else:
    print("NO")
            
