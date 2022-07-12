def solve(a,b,n):
    if a>b:
        if a==b+1 and b==n//2:
            l=[]
            r=[]
            for i in range(0,n//2):
                l.append(a+i)
                r.append(b-i)
            print(*(l+r))
            return
        print(-1)
        return
    r=[b]
    l=[a]
    lr=1
    ll=1
    for i in range(b+1,n+1):
        l.append(i)
        ll+=1
        if(ll>n//2):
            print(-1)
            return
    for i in range(1,a):
        r.append(i)
        lr+=1
        if(lr>n//2):
            print(-1)
            return
    for i in range(a+1,b):
        if(ll<n//2):
            l.append(i)
            ll+=1
        elif lr<n//2:
            r.append(i)
            lr+=1
        else:
            print(-1)
            return
    print(*(l+r))

t = int(input())
while t:
    n,a,b=map(int, input().split())
    solve(a,b,n)
    t-=1