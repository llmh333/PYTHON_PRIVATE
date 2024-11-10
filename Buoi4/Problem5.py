def Binary_Search(a,x):
    l = 0
    r = len(a)-1
    while(l <= r):
        mid = int((l+r)/2)
        if (a[mid] == x):
            return mid
        elif (a[mid] < x):
            l = mid + 1
        elif (a[mid] > x):
            r = mid - 1
    if (l >= r): 
        return -1

n = int(input("N = "))
x = int(input("X = "))
print("Lst = ")
a = [int(input()) for _ in range(n)]
a.sort()
print(a)
res = Binary_Search(a,x)
print(res)
