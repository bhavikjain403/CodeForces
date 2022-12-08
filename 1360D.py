class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n,k=map(int,input().split())
        if k>=n:
            print("1")
            return
        ans=n
        i=1
        while i*i<=n:
            if n%i==0:
                if i<=k:
                    ans=min(ans,n//i)
                if n//i<=k:
                    ans=min(ans,i)
            i+=1
        print(ans)

obj=solve()