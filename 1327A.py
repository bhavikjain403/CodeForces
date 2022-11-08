class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n,k=map(int,input().split())
        if n%2==k%2 and n>=k*k:
            print("YES") 
        else:
            print("NO")

obj=solve()