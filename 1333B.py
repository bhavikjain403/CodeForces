class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        id,idx=float('inf'),float('inf')
        for i in range(n):
            if a[i]==1:
                id=i
                break
        for i in range(n):
            if a[i]==-1:
                idx=i
                break
        for i in range(n):
            if a[i]<b[i] and id>=i:
                print("NO")
                return
            elif a[i]>b[i] and idx>=i:
                print("NO")
                return
        print("YES")

obj=solve()