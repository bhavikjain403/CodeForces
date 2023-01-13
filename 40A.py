class solve:
    def __init__(self):
        x,y=map(int,input().split())
        p=x*x+y*y
        r=int(p**0.5)
        if r*r<p and (r+1)*(r+1)>p and (r%2 and x*y>0 or r%2==0 and x*y<0):
            print("white")
        else:
            print("black")
 
obj=solve()