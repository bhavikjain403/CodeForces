class solve:
    def __init__(self):
        n,m=map(int,input().split())
        row,col=set(),set()
        ans=n*n
        result=[0]*m
        c=0
        for i in range(m):
            x,y=map(int,input().split())
            row.add(x)
            col.add(y)
            lx,ly=len(row),len(col)
            result[i]=max(0,n*n-n*(lx+ly)+lx*ly)
        print(*result)

obj=solve()