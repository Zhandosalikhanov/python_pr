s1 = input()
s = []
for c in s1:
    s.append(c)

a = []
op_brack = "({["
cl_brack = ")}]"

ans = "Yes"
for c in s:
    if op_brack.find(c) != -1:
        a.append(c)
    else:
        l = len(a) - 1
        if cl_brack.find(c) != -1 and l == -1:
            ans = "No"
            break

        if cl_brack.find(c) == op_brack.find(a[l]):
            a.pop(l)
        elif cl_brack.find(c) != op_brack.find(a[l]):
            ans = "No"
            break
        else:
            b = a
            b.reverse()
            a.pop(len(a) + 1 - b.index(op_brack[cl_brack.find(c)]))
    
if len(a) != 0:
    print("No")
else:
    print(ans)