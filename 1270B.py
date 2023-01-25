class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(n-1):
            if abs(a[i]-a[i+1])>=2:
                print("YES")
                print(i+1,i+2)
                return
        print("NO")
 
obj=solve()