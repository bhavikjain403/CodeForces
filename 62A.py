class solve:
    def __init__(self):
        g=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if (g[0]-1<=b[1] and b[1]<=2*(g[0]+1)) or (g[1]-1<=b[0] and b[0]<=2*(g[1]+1)):
            print("YES") 
        else:
            print("NO")
 
obj=solve()