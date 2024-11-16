n = int(input("So luong phan tu: "))
my_dict = {}
for i in range(n):
    key = input(f"Key thu {i+1}: ")
    value = input(f"Value thu {i+1}: ")
    my_dict[key] = value
    
new_dict = {}
for key in my_dict.keys():
    if (my_dict[key] in new_dict.keys()):
        print("None")
        exit()
    new_dict[my_dict[key]] = key
print(f"Dict sau khi hoan doi {new_dict}")