class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==0:
            if a[0]==0:
                print("YES")
            else:
                print("NO")
            return
        prefix=[0]*n
        prefix[0]=a[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+a[i]
        if prefix[n-1]!=0:
            print("NO")
        else:
            pos,v=1,0
            for i in prefix:
                if i<0:
                    pos=0
                    break
            for i in prefix:
                if i==0:
                    v=1
                elif v:
                    pos=0
            if pos:
                print("YES")
            else:
                print("NO")

obj=solve()