t=int(input())
while t:
    n=int(input())
    ans=""
    d=9
    while(n>d):
        ans=str(d)+ans
        n-=d
        d-=1
    if (n>0):
        ans=str(n)+ans
    print(ans)
    t-=1