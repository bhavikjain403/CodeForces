class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def recur(self,a,k):
        if k==1:
            return a
        mini,maxi=9,0
        temp=a
        while temp:
            maxi=max(maxi,temp%10)
            mini=min(mini,temp%10)
            temp//=10
        if mini==0:
            return a
        return self.recur(a+mini*maxi,k-1)

    def solution(self):
        n,k=map(int,input().split())
        print(self.recur(n,k))

obj=solve()