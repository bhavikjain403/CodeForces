class solve:
    def __init__(self):
        a=sum(list(map(int,input().split())))
        if a%5 or a==0:
            print("-1")
        else:
            print(a//5)

obj=solve()