class solve:
    def __init__(self):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        a.sort()
        if k==0:
            if a[0]>1:
                print(1)
            else:
                print(-1)
        elif k==n:
            print(a[k-1])
        else:
            if a[k]!=a[k-1]:
                print(a[k-1])
            else:
                print(-1)
obj=solve()