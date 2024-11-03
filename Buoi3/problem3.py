def xeploai(name,bai1,bai2):
    temp = bai1+bai2
    if (temp >= 190):
        return "Xuat sac"
    elif (temp >= 150 and temp < 190):
        return "Gioi"
    elif (temp >=100 and temp < 150):
        return "Kha"
    else:
        return "Yeu"
    
    
    
n = int(input())
for i in range(n):
    name = input()
    bai1 = int(input())
    bai2 = int(input())
    print(f"{i+1} {name} {bai1+bai2} {xeploai(name,bai1,bai2)}")