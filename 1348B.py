class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        a=set(a)
        l=len(a)
        if l>k:
            print("-1")
            return
        a=list(a)
        while l<k:
            a.append(1)
            l+=1
        print(n*k)
        for i in range(n):
            print(*a,end=" ")
        print()
 
obj=solve()