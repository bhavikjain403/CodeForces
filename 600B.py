from bisect import bisect_right

class solve:
    def __init__(self):
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        for i in range(m):
            print(bisect_right(a,b[i]),end=" ")

obj=solve()