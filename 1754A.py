class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=input()
        ans=0
        for i in a:
            if i=='Q':
                ans+=1
            else:
                ans-=1
            ans=max(ans,0)
        if ans==0:
            print("Yes")
        else:
            print("No")
 
obj=solve()