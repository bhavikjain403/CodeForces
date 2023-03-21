class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b=map(int,input().split())
        a,b=abs(a),abs(b)
        ans=2*min(a,b)
        if a==b:
            print(ans)
            return
        x,y=min(a,b),min(a,b)
        print(ans+2*(a-x+b-y)-1)
 
obj=solve()