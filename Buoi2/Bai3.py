print("Chao mung den CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc khoa CNTT - "10 diem"')
s = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
s1 = ""
print("Cac chu cai in hoa trong chuoi: ", end = "")
slower = []
supper = []
for x in s:
    if (x.isupper()):
        slower += x
        s1 += x.lower()
        
    if (x.islower()):
        supper += x
        s1 += x.upper()
    if (x == " "):
        s1 += " "
print("Cac chu cai in hoa trong chuoi: ", slower)
print("Cac chu cai in thuong trong chuoi: ", supper)

if ("CNTT" in s):
    print("YES")
else:
    print("NO")
    
print(s1)