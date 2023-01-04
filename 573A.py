class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(n):
            while a[i]%2==0:
                a[i]//=2
            while a[i]%3==0:
                a[i]//=3
        for i in range(1,n):
            if a[i]!=a[0]:
                print("No")
                return
        print("Yes")
 
obj=solve()