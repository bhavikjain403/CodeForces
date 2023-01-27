class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        pi="3141592653589793238462643383279"
        ans=0
        n=len(s)
        for i in range(n):
            if s[i]==pi[i]:
                ans+=1
            else:
                break
        print(ans)
 
obj=solve()