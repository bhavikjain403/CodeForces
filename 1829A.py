class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        t="codeforces"
        ans=0
        for i in range(10):
            if s[i]!=t[i]:
                ans+=1
        print(ans)
 
obj=solve()