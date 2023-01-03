class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        l,r=-1,-1
        for i in range(n):
            if s[i]=="R":
                r=i
                break
        for i in range(n):
            if s[n-1-i]=="L":
                l=n-1-i
                break
        if l==-1 or r==-1:
            print("-1")
            return
        if r>l:
            print(l+1)
        else:
            print("0")
 
obj=solve()