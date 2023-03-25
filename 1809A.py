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
        s=input()
        a=[0]*10
        for i in s:
            a[int(i)]+=1
        m=max(a)
        if m==4:
            print(-1)
        elif m==3:
            print(6)
        else:
            print(4)
 
obj=solve()