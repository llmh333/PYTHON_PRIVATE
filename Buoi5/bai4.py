import random
n = int(input("So luong tai khoan: "))

account = {}

for i in range(n):
    temp = {}
    acc = f"Account{i+1}"
    user = input(f"Username: ")
    while(len(user) != 10):
        print("Username phai la ma sinh vien co do dai la 10!!")
        user = input(f"Username: ")
    list_pass = ["CNTT","KHMT","KTPM","HTTT","DAPT"]
    password = random.choice(list_pass) + user
    temp["Username"] = user
    temp["Password"] = password 
    account[acc] = temp
print(account)