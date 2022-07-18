t=int(input())
while t:
    n,b,x,y=map(int,input().split())
    ans=[0]
    for i in range(1,n+1):
        if(ans[i-1]+x<=b):
            ans.append(ans[i-1]+x)
        else:
            ans.append(ans[i-1]-y)
    print(sum(ans))
    t-=1