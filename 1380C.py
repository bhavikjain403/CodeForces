class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,x=map(int,input().split())
        a=sorted(list(map(int,input().split())),reverse=True)
        ans,c=0,1
        for i in a:
            if i*c>=x:
                ans+=1
                c=0
            c+=1
        print(ans)

obj=solve()