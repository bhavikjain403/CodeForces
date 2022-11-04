class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if a[0]==min(a):
            print("Bob")
        else:
            print("Alice")

obj=solve()