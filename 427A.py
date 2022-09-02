n=int(input())
l=list(map(int,input().split()))
p,c,ans=0,0,0
for i in l:
    if i!=-1:
        p+=i
    else:
        if p<=0:
            ans+=1
        else:
            p-=1
print(ans)