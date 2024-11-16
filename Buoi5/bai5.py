docker_compose = {
    "version" : "3.8",
    "services" : "app",
    "image" : "python:3.10-slim",
    "command" : "python app.py",
    "volumes" : "./app:/app",
    "restart" : "always",
    "ports" : "5000:5000",
    "depends_on" : "db"
}

print(docker_compose)

docker_compose["version"] = '3.10'
print(docker_compose)

print(docker_compose["image"])

docker_compose["environment"] = "PYTHONUNBUFFERED=1"
print(docker_compose)

if ("volumes" in docker_compose.keys()):
    print("dict co chua key volumes")
else:
    print("dict khong chua key volumes")

docker_compose.pop("depends_on")
print(docker_compose)

print(f"So luong key cua dict: {len(docker_compose.keys())}")

temp = docker_compose.values()
print(f"Tat ca gia tri cua dict: {temp}")

if ("always" in docker_compose.values()):
    print("always co la values cua 1 key nao do")
else:
    print("always khong la values cua 1 key nao do")
    
new_key = input("New key: ")
new_value = input("New value: ")

docker_compose[new_key] = new_value
print(docker_compose)
    
    