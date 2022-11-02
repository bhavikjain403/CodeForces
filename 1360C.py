class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        e,o=0,0
        for i in a:
            if i%2:
                o+=1
            else:
                e+=1
        if e%2==0 and o%2==0:
            print("YES")
        else:
            a.sort()
            for i in range(n-1):
                if a[i+1]==a[i]+1:
                    print("YES")
                    return
            print("NO")

obj=solve()