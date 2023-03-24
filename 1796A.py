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
        n=input()
        s=input()
        if s in self.fb:
            print("YES")
        else:
            print("NO")
 
obj=solve()