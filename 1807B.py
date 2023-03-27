class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        e,o=0,0
        for i in a:
            if i%2:
                o+=i
            else:
                e+=i
        print("YES" if e>o else "NO")

 
obj=solve()