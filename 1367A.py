t=int(input())
while t:
    s=input()
    l=len(s)
    if l==2:
        print(s)
    else:
        ans=s[0]+s[1]
        for i in range(3,l):
            if i%2:
                ans+=s[i]
        print(ans)
    t-=1