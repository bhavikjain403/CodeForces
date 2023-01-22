class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        total=sum(a)
        ans=total
        for i in range(n-1):
            ans+=total
            total-=a[i]
        print(ans)

obj=solve()