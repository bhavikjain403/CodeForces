class solve:
    def __init__(self):
        n,m,a,b=map(int,input().split())
        print(min(n*a,((n//m)*b))+min(b,((n%m)*a)))

obj=solve()