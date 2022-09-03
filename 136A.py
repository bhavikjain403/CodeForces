n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(1,n+1):
    ans.append(a.index(i)+1)
print(*ans)