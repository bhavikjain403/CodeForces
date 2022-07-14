t = int(input())
while t:
    n = int(input())
    s = list(input())
    r = -1
    b = -1
    for i in range(n):
        if s[i]=="R":
            r=i
            break
        if s[i]=="B":
            b=i
            break
    if s[0]=="?":
        ans = ""
        if r>-1:
            if r%2==0:
                ans+="R"
            else:
                ans+="B"
        elif b>-1:
            if b%2==0:
                ans+="B"
            else:
                ans+="R"
        else:
            ans+="B"
    else:
        ans=s[0]
    for i in range(1,n):
        if s[i]=="?":
            if ans[i-1]=="R":
                ans+="B"
            else:
                ans+="R"
        else:
            ans+=s[i]
    print(ans)
    t-=1