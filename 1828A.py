class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        ans=0
        a=[0]*(n+1)
        for i in range(n,1,-1):
            a[i]=i
            ans=(ans+i)%n
        a[1]=n-ans
        for i in range(1,n+1):
            print(a[i],end=' ')
        print()
    
obj=solve()