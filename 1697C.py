class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        t=input()
        if s.count("b")!=t.count("b"):
            print("NO")
            return
        j=0
        for i in range(n):
            if s[i]=="b":
                continue
            while t[j]=="b":
                j+=1
            if s[i]!=t[j] or (s[i]=="a" and i>j) or (s[i]=="c" and i<j):
                print("NO")
                return
            j+=1
        print("YES")

obj=solve()