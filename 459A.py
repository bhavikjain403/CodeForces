class solve:
    def __init__(self):
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2:
            s=abs(y1-y2)
            if s==0:
                print(-1)
            else:
                print(x1+s,y1,x1+s,y2)
        elif y1==y2:
            s=abs(x1-x2)
            if s==0:
                print(-1)
            else:
                print(x1,y1+s,x2,y1+s)
        elif x1!=x2 and y1!=y2:
            sx=abs(x1-x2)
            sy=abs(y1-y2)
            if sx!=sy:
                print(-1)
            else:
                print(x1,y2,x2,y1)
        else:
            print(-1)

obj=solve()