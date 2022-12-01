class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        m=int(input())
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        ans=0
        for i in range(n):
            for j in range(m):
                if abs(a[i]-b[j])<2:
                    ans+=1
                    b[j]=1000
                    break
        print(ans)

obj=solve()