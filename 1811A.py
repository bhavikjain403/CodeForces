class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,d=map(int, input().split())
        d=str(d)
        num=input()
        if d=="0":
            print(num+d)
        else:
            i=0
            while i<n and num[i]>=d:
                i+=1
            if i==n:
                print(num+d)
            else:
                print(num[:i]+d+num[i:])
 
obj=solve()