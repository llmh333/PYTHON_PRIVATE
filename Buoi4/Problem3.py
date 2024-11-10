n = int(input("N = "))
print("nums1 = ")
a = [input() for _ in range(n)]

m = int(input("M = "))
print("nums2 = ")
b = [input() for _ in range(m)]

c = []

for i in range(n):
    if (a[i] in b):
        c.append(a[i])
        
print(c)    