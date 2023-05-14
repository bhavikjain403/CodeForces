class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        ans=0
        for i in range((n-1)//2,-1,-1):
            if s[i]==s[(n-1)//2]:
                ans+=1
            else:
                break
        print(2*ans-(n&1))
 
obj=solve()