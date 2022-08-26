t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().split()))
    s=len(set(l))
    if n!=s:
        print("0")
    else:
        ans=float('inf')
        l.sort()
        for i in range(0,n-1):
            ans=min(ans,l[i+1]-l[i])
        print(ans)
    t-=1