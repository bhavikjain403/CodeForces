class solve:
    def __init__(self):
        n=int(input())
        while n!=1:
            print(n,end=" ")
            for i in range(2,n+1):
                if n%i==0:
                    n//=i
                    break
        print(n)
 
obj=solve()