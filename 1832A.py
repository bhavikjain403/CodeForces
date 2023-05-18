class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        l=len(set(s[:len(s)//2]))
        if l==1:
            print("NO")
        else:
            print("YES")
 
obj=solve()