t=int(input())
while t:
    a=list(map(int,input().split()))
    if a[0]+a[1]+a[2]==a[-1]:
        print(a[0],a[1],a[2])
    else:
        print(a[0],a[1],a[3])
    t-=1