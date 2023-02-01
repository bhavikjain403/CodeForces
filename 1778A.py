class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        tot=sum(a)
        flag3=0
        for i in range(n-1):
            if a[i]==-1 and a[i+1]==-1:
                print(tot+4)
                return
            if a[i]==-1 and a[i+1]==1:
                flag3=1
            if a[i]==1 and a[i+1]==-1:
                flag3=1
        if flag3==1:
            print(tot)
        else:
            print(tot-4)
 
obj=solve()