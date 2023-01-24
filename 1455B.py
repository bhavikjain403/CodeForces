class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        ans=0
        while ans*(ans+1)<2*n:
            ans+=1
        if (ans*(ans+1))//2==n+1:
            print(ans+1)
        else:
            print(ans)
 
obj=solve()