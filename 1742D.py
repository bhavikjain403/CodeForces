from math import gcd

t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    s,data,d,ans=set(),[],{},0
    for i in range(n):
        d[a[i]]=i+1
        if a[i] not in s:
            s.add(a[i])
            data.append(a[i])
    l=len(data)
    for i in range(l):
        for j in range(l):
            if gcd(data[i],data[j])==1:
                ans=max(d[data[i]]+d[data[j]],ans)
    if ans:
        print(ans)
    else:
        print("-1")
    t-=1