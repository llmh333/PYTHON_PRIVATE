a = int(input("Nhap a:"))
luu = a

dem = 0

while(a > 0):
    temp = a%8
    a = a // 8
    dem += 1
print("So luong bit de bieu dien ", luu, " o he phat phan: ", dem)

b = float(input("Nhap so bat ky: "))

attri = dir(b)
print("cac thuoc tinh va phuong thuc hien tai cua ", b)
for x in attri:
    print(x)

