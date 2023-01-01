class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if a[i]>=a[j]:
                    ans+=1
        print(ans)

obj=solve()