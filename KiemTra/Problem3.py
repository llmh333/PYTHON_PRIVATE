def solve(code):
    code = str(code)
    ans = ""
    for i in range(len(code)):
        if (code[i] != "[" and code[i] != "]" and code[i].isdigit() == False):
            ans += code[i]
        if (code[i].isdigit()):
            temp = int(code[i])
            s1 = ""
            j = i+2
            while(j < len(code)):
                if (code[j] == "]"):
                    break
                s1 += code[j]
                j += 1
            s1 = s1*(temp-1)
            ans += s1
    return ans
code_str = input()
ans = solve(code_str)
print(ans)