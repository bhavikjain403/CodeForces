class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print("YES")
            return
        i=0
        while i<n-1 and a[i]>=a[i+1]:
            i+=1
        if i==n-1:
            print("YES")
            return
        for j in range(i,n-1):
            if a[j]>a[j+1]:
                print("NO")
                return
        print("YES")

obj=solve()