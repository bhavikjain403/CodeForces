class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a1,a2,a3,a4=map(int,input().split())
        if a1==0:
            print(1)
            return
        print(a1+min(a2,a3)*2+min(a1+1,a4+abs(a2-a3)))
 
obj=solve()