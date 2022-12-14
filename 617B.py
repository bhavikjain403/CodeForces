class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        idx=-1
        ans=0
        for i in range(n):
            if a[i]==1:
                if idx==-1:
                    ans=1
                else:
                    ans*=i-idx
                idx=i
        print(ans)

obj=solve()