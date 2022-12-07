class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if len(set(b))==1:
            temp=sorted(a)
            if a!=temp:
                print("No")
            else:
                print("Yes")
        else:
            print("Yes")

obj=solve()