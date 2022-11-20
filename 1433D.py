class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if a.count(a[0])==n:
            print("NO")
            return
        print("YES")
        idx=-1
        for i in range(1,n):
            if a[i]!=a[0]:
                idx=i
                print(f"1 {i+1}")
        for i in range(1,n):
            if a[i]==a[0]:
                print(f"{idx+1} {i+1}")

obj=solve()