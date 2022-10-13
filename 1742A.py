t=int(input())
while t:
    a=list(map(int,input().split()))
    a.sort()
    if a[2]==a[0]+a[1]:
        print("YES")
    else:
        print("NO")
    t-=1