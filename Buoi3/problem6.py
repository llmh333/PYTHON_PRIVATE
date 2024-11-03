import math
def binary(x):
    return 0 if (x < 0) else 1

def sigmoid(x):
    return 1/(1+math.e**(-x))

def ELU(x):
    alpha = 0.01
    return alpha*(math.e**(x)-1) if (x < 0) else x


x = input()

try:
    x = float(x)
except:
    print("X must be a number")
    exit()

select = input("Inpu tactivation Function ( binary | sigmoid | elu ): ")




if (select == "binary"):
    print(binary(x))
elif (select == "sigmoid"):
    print(sigmoid(x))
elif (select == "elu"):
    print(ELU(x))
else:
    print(f"{select} is not supported")