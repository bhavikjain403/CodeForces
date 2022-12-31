class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        if k==1:
            for i in range(1,n+1):
                print(i,end=" ")
        else:
            l,h=1,n
            for i in range(n):
                if i%2:
                    print(l,end=" ")
                    l+=1
                else:
                    print(h,end=" ")
                    h-=1
        print()

obj=solve()