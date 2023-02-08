class solve:
    def __init__(self):
        n=int(input())
        sieve=[0]*100005
        for i in range(2,n+2):
            if sieve[i]==0:
                j=2*i
                while j<n+2:
                    sieve[j]=1
                    j+=i
        if n<=2:
            print(1) 
        else:
            print(2)
        for i in range(2,n+2):
            if sieve[i]:
                print("2",end=" ")
            else:
                print("1",end=" ")
 
obj=solve()