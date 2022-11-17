class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        e,o=0,0
        for i in a:
            if i%2:
                o+=1
            else:
                e+=1
        d=x-min(x-1,e)
        if d%2==0:
            d+=1
        if o>=d and d<=x:
            print("Yes")
        else:
            print("No")

obj=solve()