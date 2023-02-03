class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans,mini=sum(a),-float('inf')
        c,s=0,0
        for i in a:
            temp=abs(i)
            s+=temp
            if i<0:
                c+=1
            mini=max(mini,-temp)
        if c%2==0:
            mini=0
        print(max(2*mini+s,ans))

obj=solve()