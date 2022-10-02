n,k=map(int,input().split())
d1,d2=dict(),dict()
a,b=[0]*(n+1),[0]*1001
ans=0
for i in range(1,n+1):
    temp=0
    a[i]=list(map(int,input().split()))
    for j in range(k):
        temp*=3
        temp+=a[i][j]
    if temp not in d1:
        d1[temp]=1
    else:
        d1[temp]+=1
    b[i]=temp
for i in range(1,n):
    for j in range(i+1,n+1):
        temp=0
        for x in range(k):
            temp*=3
            if a[i][x]==a[j][x]:
                temp+=a[i][x]
            else:
                temp+=3-a[i][x]-a[j][x]
        if temp not in d1:
            continue
        cpy=d1[temp]
        if not b[i] in d2:
            d2[b[i]]=cpy
        else:
            d2[b[i]]+=cpy
        if not b[j] in d2:
            d2[b[j]]=cpy
        else:
            d2[b[j]]+=cpy
        if not temp in d2:
            d2[temp]=cpy
        else:
            d2[temp]+=cpy
for i in d2:
    ans+=d2[i]//3*(d2[i]//3-1)//2
print(ans)