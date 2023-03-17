class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        if n==5 and 'T' in s and 'i' in s and 'm' in s and 'u' in s and 'r' in s:
            print("YES")
        else:
            print("NO")
 
obj=solve()