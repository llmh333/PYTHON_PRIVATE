def GT(n):
    tich = 1
    for i in range(2,n+1):
        tich *= i
    return tich

def ex(x):
    tong = 0
    for i in range(100):
        tong += (x**i)/(GT(i))
    return tong
x = float(input())
res = ex(x)
print(res)