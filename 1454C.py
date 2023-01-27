from collections import Counter

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if len(set(a))==1:
            print("0")
            return
        c=Counter(a)
        c[a[0]]-=1
        c[a[n-1]]-=1
        print(min(c.values())+1)
 
obj=solve()