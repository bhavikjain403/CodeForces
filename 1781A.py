class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        w,d,h=map(int,input().split())
        a,b,f,g=map(int,input().split())
        print(h+min(a+abs(b-g)+f,b+abs(a-f)+g,(d-b)+abs(a-f)+(d-g),(w-a)+abs(b-g)+(w-f)))
 
obj=solve()