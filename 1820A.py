class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        if s=='^':
            print(1)
            return
        ans=0
        if s[0]=='_':
            ans+=1
        if s[-1]=='_':
            ans+=1
        for i in range(len(s)-1):
            if s[i]=='_' and s[i+1]=="_":
                ans+=1
        print(ans)
 
obj=solve()