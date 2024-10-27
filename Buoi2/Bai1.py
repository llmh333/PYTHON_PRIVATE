a = int(input("A = "))
b = int(input("B = "))

print("A + B = ", a+b)

print("A - B = ", a-b)

print("A * B = ", a*b)

print("A // B = ", a//b)

print("A ^ B = ", pow(a,b))

print("A % B = ", a%b )

if (a >=b ): 
    print("A >= B")
else: 
    print("A < B")

print("A and B = ", a & b)

print("A or B = ", a | b)

print("A xor B = ", a ^ b, end="\n")

print("NOT A == B: ", not(a==b))

print("A dich trai 5 bit = ", a << 5)

print("A dich phai 5 bit = ", a >> 5)


if (a == 0): print("0")
else:
    s = ""
    while (a > 0):
        temp = a%2
        a = a // 2
        s = str(temp) + s
print(s)