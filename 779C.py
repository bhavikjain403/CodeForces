class solve:
    def __init__(self):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        data=[]
        for i in range(n):
            data.append([i,a[i]-b[i]])
        data.sort(key=lambda x:x[1])
        ans=0
        for i in range(n):
            if i<k:
                ans+=a[data[i][0]]
            else:
                ans+=min(a[data[i][0]],b[data[i][0]])
        print(ans)

obj=solve()