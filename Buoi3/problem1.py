def GT(x):
    temp = 1
    for i in range(1,x+1):
        temp *= i
    return temp

def ex(x):
    tong = 1
    for i in range (1,100):
        tong += (x**i)/(GT(i))
    return tong

def S(n):
    tong = 1
    for i in range (2,n+1):
        tong += 1/(GT(i))
    return tong

x = int(input("Nhap x = "))
n = int(input("Nhap n = "))

print(ex(x))
print(S(n))