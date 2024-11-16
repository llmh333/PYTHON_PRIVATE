import math
a = {"Nguyen Van A","Tran Thi B","Le Van C","Nguyen Minh D","Tran Minh Tri"}
b = {"Nguyen Van A","Le Van C"}

c = a.difference(b)
if (c == {}):
    print("Tat ca da check in")
else:
    print("Danh sach cac ban chua check in: ",end="")
    print(c)

print("So luong cac ban da dang ky: " + str(len(a)))
print("So luong cac ban da check in: " + str(len(b)))
temp = []
sorted(a)
print(a)
