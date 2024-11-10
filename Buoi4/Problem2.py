n = int(input("N = "))
print("A[] = ")
a = [input() for _ in range(n)]

m = int(input("M = "))
print("B[] = ")
b = [input() for _ in range(m)]

i = j = 0
c = []
while(i < len(a) or j < len(b)):
    if (i < len(a) or (j == len(b)-1 and i < len(a))):
        c.append(a[i])
        i += 1
    if (j < len(b) or (i == len(a)-1 and j < len(b))):
        c.append(b[j])
        j += 1
print(c)