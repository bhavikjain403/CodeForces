n,m=map(int,input().split())
ans=0
day=0
while n:
    n-=1
    ans+=1
    day+=1
    if day%m==0:
        n+=1
print(ans)