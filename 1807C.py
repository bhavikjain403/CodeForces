class solve:
    def __init__(self):
        self.fb=""
        for i in range(1,100):
            if i%3==0:
                self.fb+="F"
            if i%5==0:
                self.fb+="B"
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        for i in range(n-1):
            for j in range(i+1,n,2):
                if s[j]==s[i]:
                    print("NO")
                    return
        print("YES")
 
obj=solve()