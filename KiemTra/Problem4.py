data = ["name=Alice;age=30;score=85.5","name=Bob;age=25;score=90","name=Alice;age=30;score=92","city=NewYork;name=Eve;age=35;score=88","city=London;name=Alice;age=30;score=85.5"]

dict = {}
result = {}
listkey = []
for i in range(len(data)):
    key = (data[i].split(";"))
    for j in range(len(key)):
        temp = key[j].split("=")
        dict[temp[0]] = []
        result[temp[0]] = []

for i in range(len(data)):
    key = (data[i].split(";"))
    for j in range(len(key)):
        temp = key[j].split("=")
        value = dict[temp[0]]
        value = list(value)
        value.append(temp[1])
        dict[temp[0]] = value


# for i in dict.keys():
#     temp = dict[i]
#     a = {}
#     for j in range(len(temp)):
#         a[temp[j]] = 1
#     res = {
#         "unique_count" : None,
#         "max_value" : None,
#         "max_length" : None
#     }
#     res["unique_count"] = len(a.keys())
#     if (type(temp[0]) == "str"):
#         res["max_value"] = None
#     else:
#         res["max_value"] = max(temp)
#     result[i] = a
#     break
print(dict)