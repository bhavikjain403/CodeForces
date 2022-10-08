from collections import Counter

k=int(input())
s=input()
c=Counter(s)
l=len(c)
if k==1:
    print(s)
else:
    v=list(c.values())
    q,r=v[0]//k,v[0]%k
    if r==0:
        v[0]=q
        flag=1
        for i in range(1,l):
            if v[i]%k==0:
                v[i]=v[i]//k
                continue
            else:
                flag=0
                break
        if flag:
            ans=""
            j=0
            for i in c:
                ans+=i*v[j]
                j+=1
            print(ans*k)
        else:
            print("-1")
    else:
        print(-1)