t=int(input())
while t:
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    x,y=min(x,y),max(x,y)
    print(min((x+y)*a, (y-x)*a+x*b))
    t-=1