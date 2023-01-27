class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        x=int(input())
        s=x*2
        a,b=0,0
        temp=(s-x)//2
        for i in range(64):
            shift=1<<i
            m,n=shift&x,shift&temp
            if m==0 and n==0:
                continue
            elif m>0 and n==0:
                a|=shift
            elif m==0 and n>0:
                a|=shift
                b|=shift
            else:
                print(-1)
                return
        if a+b==s:
            print(a,b)
        else:
            print(-1)
 
obj=solve()