t=int(input())
while t:
    x,y,n=map(int,input().split())
    q=(n//x)*x
    k=q+y
    if k<=n:
        print(k)
    else:
        print(k-x)
    t-=1