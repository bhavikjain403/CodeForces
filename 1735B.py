t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(1,n):
        temp=(a[i]-2+2*a[0])//(2*a[0]-1)
        if temp>1:
            ans+=temp-1
    print(ans)
    t-=1