from collections import Counter

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        s=input()
        c=Counter(s)
        pairs,single=0,0
        for i in c:
            pairs+=c[i]//2
            single+=c[i]%2
        single+=(pairs%k)*2
        if single>=k:
            print((pairs//k)*2+1)
        else:
            print((pairs//k)*2)

obj=solve()