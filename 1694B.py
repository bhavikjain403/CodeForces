class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        ans=n
        for i in range(n-1):
            if s[i+1]!=s[i]:
                ans+=i+1
        print(ans)

obj=solve()