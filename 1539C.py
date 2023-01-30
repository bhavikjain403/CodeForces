class solve:
    def __init__(self):
        n,k,x=map(int,input().split())
        a=list(map(int,input().split()))
        a.sort()
        d=[]
        for i in range(1,n):
            diff=a[i]-a[i-1]
            if diff>x:
                d.append((diff-1)//x)
        d.sort()
        ans=len(d)+1
        for i in range(len(d)):
            if k>=d[i]:
                k-=d[i]
                ans-=1
            else:
                break
        print(ans)

obj=solve()