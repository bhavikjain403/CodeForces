class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if a<b and c<d and a<c and b<d:
            print("YES")
        elif c<a and d<b and c<d and a<b:
            print("YES")
        elif c<a and d<b and c>d and a>b:
            print("YES")
        elif c>a and d>b and c>d and a>b:
            print("YES")
        else:
            print("NO")

obj=solve()