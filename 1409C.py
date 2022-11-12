class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n,x,y=map(int,input().split())
        if n==2:
            print(x,y)
        else:
            for i in range(n-1,0,-1):
                if (y-x)%i==0:
                    q=(y-x)//i
                    break
            d=1
            for i in range(n):
                if y-q*i>0:
                    print(f"{y-q*i} ",end="",sep="")
                else:
                    print(f"{y+q*d} ",end="",sep="")
                    d+=1
            print("")
obj=solve()