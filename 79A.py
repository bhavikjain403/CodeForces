class solve:
    def __init__(self):
        x,y=map(int,input().split())
        turn=0
        flag=0
        ans=0
        while True:
            if x>=2 and y>=2:
                x-=2
                y-=2
            elif x>=1 and y>=12:
                x-=1
                y-=12
            elif y>=22:
                y-=22
            else:
                print("Hanako")
                break
            if y>=22:
                y-=22
            elif y>=12 and x>=1:
                y-=12
                x-=1
            elif y>=2 and x>=2:
                y-=2
                x-=2
            else:
                print("Ciel")
                break

obj=solve()