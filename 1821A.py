class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        ans=1
        if s[0]=='0':
            ans=0
        if s[0]=='?':
            ans=9
        for i in range(1,len(s)):
            if s[i]=='?':
                ans*=10
        print(ans)
 
obj=solve()