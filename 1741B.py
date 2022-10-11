t=int(input())
while t:
    n=int(input())
    if n==3:
        print("-1")
    elif n%2==0:
        for i in range(n,0,-1):
            print(f"{i} ",end="")
        print()
    else:
        print(f"{n} {n-1} ",end="")
        for i in range(1,n-1):
            print(f"{i} ",end="")
        print()
    t-=1