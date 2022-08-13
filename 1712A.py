t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n==k:
        print("0")
    else:
        ans=0
        x=a[:k]
        y=a[k:]
        for i in range(k):
            if i+1 in y:
                ans+=1
        print(ans)
    t-=1