t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    ans=n
    temp=[]
    i=1
    while i*i<=total:
        if total%i==0:
            temp.append(i)
            q=total//i
            if q!=i:
                temp.append(q)
        i+=1
    if len(temp)<3:
        print(ans)
    else:
        for i in temp:
            flag=1
            x,y,z=0,0,0
            q=total//i
            for j in range(n):
                x+=a[j]
                y+=1
                if q==x:
                    x=0
                    z=max(z,y)
                    y=0
                elif q<x:
                    flag=0
                    break
            if flag:
                ans=min(ans,z)
        print(ans)
    t-=1