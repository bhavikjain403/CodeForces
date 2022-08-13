t=int(input())
while t:
    n=int(input())
    ans=[]
    for i in range(n):
        ans.append(i+1)
    i=n-1
    while i>0:
        ans[i],ans[i-1]=ans[i-1],ans[i]
        i-=2
    print(*ans)
    t-=1