class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())-1
        a,b=1,0
        if n==0:
            print(a,b)
        else:
            c,chance=2,2
            while n:
                if c+c+1<=n:
                    n-=(c+c+1)
                    if chance==2:
                        b+=c+c+1
                        chance=1
                    else:
                        a+=c+c+1
                        chance=2
                elif chance==1:
                    print(a+n,b)
                    return
                elif chance==2:
                    print(a,b+n)
                    return
                c+=2
            print(a,b)

obj=solve()