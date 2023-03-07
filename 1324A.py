class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print("YES")
        else:
            p=a[0]%2
            for i in range(1,n):
                if a[i]%2!=p:
                    print("NO")
                    return
            print("YES")
 
obj=solve()