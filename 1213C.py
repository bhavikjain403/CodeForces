class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n,m=map(int,input().split())
        data=[]
        s=0
        for i in range(10):
            data.append(((i+1)*m)%10)
            s+=data[i]
        n=n//m
        s*=n//10
        for i in range(n%10):
            s+=data[i]
        print(s)

obj=solve()