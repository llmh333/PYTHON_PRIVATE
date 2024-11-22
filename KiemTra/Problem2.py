def solve(s):
    dir = {}
    for i in range(len(s)):
        dir[s[i]] = 0
    for i in dir.keys():
        dem = 0
        for j in range(len(s)):
            if (i == s[j]):
                dem += 1
        dir[i] = dem
    return dir

s = input()
ans = solve(s)
print(ans)
