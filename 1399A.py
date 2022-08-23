t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    flag=1
    for i in range(n-1):
        if a[i+1]-a[i]<=1:
            continue
        else:
            flag=0
            print("NO")
            break
    if flag:
        print("YES")
    t-=1