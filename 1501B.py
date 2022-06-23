t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    ans = [0]*n
    k=l[n-1]
    for i in range(n-1,-1,-1):
        if(k!=0 or l[i]!=0):
            ans[i]=1
            k=max(k,l[i])
            k-=1
        else:
            k=l[i]
    print(*ans)
    t-=1