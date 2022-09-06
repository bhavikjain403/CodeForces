n=input()
c=0
for i in n:
    if i=="4" or i=="7":
        c+=1
c=str(c)
flag=1
for i in c:
    if i=="4" or i=="7":
        continue
    else:
        print("NO")
        flag=0
        break
if flag:
    print("YES")