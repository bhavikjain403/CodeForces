class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        flag=1
        for i in range(n):
            if a[i]!=i+1:
                flag=0
                print(i+1)
                break
        if flag:
            print(n+1)

obj=solve()