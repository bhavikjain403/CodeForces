class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        r1=input()
        r2=input()
        r1=r1.replace("G","B")
        r2=r2.replace("G","B")
        if r1==r2:
            print("YES")
        else:
            print("NO")
 
obj=solve()