class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a,b=[],[]
        p,q,ans=0,0,1
        for i in range(n):
            x,y=map(int,input().split())
            a.append(x)
            b.append(y)
            if x<p or y<q or x-p<y-q:
                ans=0
            p,q=x,y
        if ans:
            print("YES")
        else:
            print("NO")

obj=solve()