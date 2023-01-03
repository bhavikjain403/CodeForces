from bisect import bisect_left
class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=[0]*n
        for i in range(n):
            c[i]=a[i]-b[i]
        c.sort()
        ans=0
        for i in range(n):
            if c[i]<=0:
                continue
            idx=bisect_left(c,1-c[i])
            ans+=i-idx
        print(ans)

obj=solve()