n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(m):
    if a[i]<0:
        ans-=a[i]
    else:
        break
print(ans)