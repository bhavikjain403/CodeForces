class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        print(1,end=" ")
        for i in range(n,1,-1):
            print(i,end=" ")
        print()
 
obj=solve()