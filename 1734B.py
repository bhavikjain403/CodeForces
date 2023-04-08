class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        for i in range(1,n+1):
            for j in range(1,i+1):
                if j==1 or j==i:
                    print(1,end=" ")
                else:
                    print(0,end=" ")
            print()
 
obj=solve()