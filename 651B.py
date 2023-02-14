class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        d={}
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if d.get(j,0)==0 and a[i]<a[j]:
                    d[j]=1
                    ans+=1
                    break
        print(ans)

obj=solve()