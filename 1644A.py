t=int(input())
while t:
    s=input()
    key=[0,0,0]
    flag=1
    for i in s:
        if i=="r":
            key[0]=1
        elif i=="g":
            key[1]=1
        elif i=="b":
            key[2]=1
        elif i=="R" and key[0]!=1:
            flag=0
            break
        elif i=="G" and key[1]!=1:
            flag=0
            break
        elif i=="B" and key[2]!=1:
            flag=0
            break
    if flag:
        print("YES")
    else:
        print("NO")
    t-=1