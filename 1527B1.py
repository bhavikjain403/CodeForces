class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        s=input()
        c=s.count("0")
        if c==1:
            print("BOB")
        elif c%2:
            print("ALICE")
        else:
            print("BOB")

obj=solve()