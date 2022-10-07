n=int(input())
a=sum(list(map(int,input().split())))
ans=0
for i in range(1,6):
    if (a+i)%(n+1)!=1:
        ans+=1
print(ans)