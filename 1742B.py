t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    flag=1
    for i in range(n-1):
        if a[i]==a[i+1]:
            flag=0
            break
    if flag:
        print("YES")
    else:
        print("NO")
    t-=1