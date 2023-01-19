class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(enumerate(a))
        b.sort(key=lambda x:x[1])
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                if b[i][1]*b[j][1]>=2*n:
                    break
                ans+=(b[i][1]*b[j][1]==b[i][0]+b[j][0]+2)
        print(ans)
 
obj=solve()