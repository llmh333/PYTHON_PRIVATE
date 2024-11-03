m = int(input())


daily_descriptions = []
total_food = 0
top_eater = ""
max_eater = 0
min_eater = 101
lowest_eater_index = 0
couplename = []
couplethucan = []
for i in range(m):
    name = input()
    thucan = int(input())
    if (thucan <= 100):
        if (thucan >=5): 
            total_food += thucan
        couplename.append(name)
        couplethucan.append(thucan)
        if (max_eater < thucan):
            max_eater = thucan
            top_eater = name
        if (min_eater > thucan):
            min_eater = thucan
            lowest_eater_index = i+1;
    else:
        break

daily_descriptions = zip(couplename,couplethucan)
            
for x in daily_descriptions:
    print(x)
print(f"Tong luong thuc an can cho cac loai: {total_food}")
print(f"Loai an nhieu thuc an nhat: {top_eater}")
if (lowest_eater_index == 0):
    print("Khong co loai co luong an thap nhat")
else:
    print(f"Chi so loai co luong an thap nhat: {lowest_eater_index}")