LopHoc = []

n = int(input("So luong hoc vien HIT15: "))

for i in range(n):
    print("--Thong tin ban thu ", i+1, "--")
    Ten = input("Ho va Ten: ")
    Tuoi = int(input("Tuoi: "))
    GioiTinh = input("Gioi tinh: ")
    Marry = input("Tinh trang hon nhan: ")
    
    person = {
        "Ten" : Ten,
        "Tuoi" : Tuoi,
        "Gioi Tinh" : GioiTinh,
        "Hon nhan" : Marry
    }
    
    LopHoc.append(person)
for x in LopHoc:
    print(x)