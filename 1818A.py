class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        ans=n
        t=[]
        for i in range(n):
            t.append(input())
            if t[0]!=t[i]:
                ans-=1
        print(ans)
 
obj=solve()