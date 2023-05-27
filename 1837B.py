class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        ans,cur=1,1
        for i in range(1,n):
            if s[i]!=s[i-1]:
                cur=1
            else:
                cur+=1
            ans=max(ans,cur)
        print(ans+1)
    
obj=solve()