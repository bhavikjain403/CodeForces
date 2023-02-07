class solve:
    def __init__(self):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        maxi=max(a,b,c,d)
        for i in range(maxi+1):
            for j in range(maxi+1):
                if a*i+b==c*j+d:
                    print(a*i+b)
                    return
        print("-1")
 
obj=solve()