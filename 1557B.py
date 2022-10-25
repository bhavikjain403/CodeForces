t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n==1:
        if k==1:
            print("YES")
        else:
            print("NO")
    else:
        ans=1
        b=sorted(a)
        d=dict()
        for i in range(n):
            d[b[i]]=i
        for i in range(1,n):
            if a[i]>=a[i-1] and d[a[i]]==d[a[i-1]]+1:
                continue
            else:
                ans+=1
            if ans>k:
                break
        if ans<=k:
            print("YES")
        else:
            print("NO")
    t-=1