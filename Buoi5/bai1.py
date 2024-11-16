import math
n = int(input("So luong phan tu tuple A: "))
a = tuple([int(input()) for _ in range(n)])

m = int(input("So luong phan tu tuple B: "))
b = tuple([input() for _ in range(m)])
k = input("Nhap ky tu K = ")

avg = sum(a)/len(a)

d = [a[i] for i in range(n) if (a[i]>avg)]

if (d == []):
    print("Khong co phan tu nao lon hon trung binh cong cua tuple")
else:
    print("Co " + str(len(d)) + " phan tu lon hon trung binh cong")
    
a1 = tuple([a[i] for i in range(n) if (a[i]%2==0)])
a2 = tuple([a[i] for i in range(n) if (a[i]%2==1)])

dem = 0
b1 = []
for i in range(m):
    if (k in b[i]):
        dem += 1
    if (len(b[i]) >= 5):
        b1.append(b[i])
if (dem == 0):
    print("Khong co ky tu K nao trong B")
else:
    print("Co " + str(dem) + " ky tu K trong B")
    
if (b1 == []):
    print("Khong co phan tu nao co do dai lon hon 5 ky tu")
else:
    print("Cac phan tu co do dai lon hon 5 ky tu: " + str(b1))
    
c = zip(a,b)
print("A va B sau khi ket hop: " + str(tuple(c)))