class solve:
    def __init__(self):
        n,l=map(int,input().split())
        a=list(map(int,input().split()))
        a.sort()
        d=0
        for i in range(n-1):
            d=max(d,a[i+1]-a[i])
        m=max(a[0],l-a[n-1])
        if m>=d/2:
            print(m)
        else:
            print(d/2)

obj=solve()