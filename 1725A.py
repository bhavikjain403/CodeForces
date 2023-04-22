class solve:
    def __init__(self):
        n,m=map(int,input().split())
        if m>1:
            print(n*(m-1))
        else:
            print(n-1)
 
obj=solve()