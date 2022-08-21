t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    amin=min(a)
    bmin=min(b)
    ans=0
    for i in range(n):
        if a[i]>amin and b[i]>bmin:
            ans+=max(a[i]-amin,b[i]-bmin)
        elif a[i]>amin:
            ans+=a[i]-amin
        elif b[i]>bmin:
            ans+=b[i]-bmin
    print(ans)
    t-=1