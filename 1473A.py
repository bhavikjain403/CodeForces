t=int(input())
while t:
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    if a[0]<=d and a[0]==a[-1]:
        print("YES")
    elif a[-1]<=d:
        print("YES")
    elif a[0]+a[1]<=d:
        print("YES")
    else:
        print("NO")
    t-=1