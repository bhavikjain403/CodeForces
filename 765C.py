class solve:
    def __init__(self):
        k,a,b=map(int,input().split())
        if a%k==0 and b<k:
            ans=a//k
        elif b%k==0 and a<k:
            ans=b//k
        elif a>=k and b>=k:
            ans=a//k+b//k
        else:
            ans=-1
        if ans<=0:
            print(-1)
        else:
            print(ans)

obj=solve()