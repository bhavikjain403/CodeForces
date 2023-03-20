class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b,c,d= map(int, input().split())
        if d<b:
            print(-1)
        elif d==b and c>a:
            print(-1)
        elif c>a+d-b:
            print(-1)
        else:
            print(d-b+abs(d-b+a-c))
 
obj=solve()