t=int(input())
while t:
    n=int(input())
    s=input()
    ans=""
    for i in s:
        if i=="U":
            ans+="D"
        elif i=="D":
            ans+="U"
        else:
            ans+=i
    print(ans)
    t-=1