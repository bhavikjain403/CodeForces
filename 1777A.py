class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c=0
        i=0
        if n==0:
            print(c)
        else:
            while i<n-1:
                if a[i]%2==a[i+1]%2:
                    c+=1
                i+=1
            print(c)
 
obj=solve()