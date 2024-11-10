import random,math

def check(lossname):
    switcher = {
        "MAE" : 1,
        "MSE" : 2,
        "RMSE": 3,
        "Huber_Loss" : 4
    }
    
    return switcher.get(lossname,"loss name loss is not supported")


def start(n):
    y = [random.randint(0,10) for _ in range(n)]
    yy = [random.randint(0,10) for _ in range(n)]
    return y,yy

def MAE(y,yy,n):
    res = 0
    for i in range(n):
        res += abs(y[i]-yy[i])
    return res*(1/n)

def MSE(y,yy,n):
    res = 0
    for i in range(n):
        res += pow(y[i]-yy[i],2)
    return res*(1/n)
    
def RMSE(y,yy):
    res = math.sqrt(MSE(y,yy))

def Huber_Loss(y,yy,n):
    phi = 0.5
    res = 0
    for i in range(n):
        temp = y[i]-yy[i]
        if (abs(temp) <= phi):
            res += (1/2)*pow(temp,2)
        else:
            res += phi*abs(temp) - phi/2
    return res*(1/n)


n = int(input("N = "))
if (n != int(n)):
    print("number of samples must be a postive integer number")
    exit()
else:
    lossname = input("Input loss name(MAE, MSE, RMSE, Huber_Loss):")
    kt = check(lossname)
    if (kt == "loss name loss is not supported"):
        # print("loss name loss is not supported")
        exit()
    else:
        a = start(n)
        print(a[0],a[1])
        if (kt == 1):
            res = MAE(a[0],a[1],n)
        elif (kt == 2):
            res = MSE(a[0],a[1],n)
        elif (kt == 3):
            res = RMSE(a[0],a[1])
        elif (kt == 4):
            res = Huber_Loss(a[0],a[1],n)
        print(res)
        
            
            
