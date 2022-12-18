class solve:
    def __init__(self):
        n=int(input())
        s=input()
        if n==1:
            print("0")
        else:
            r1,b1,r2,b2=0,0,0,0
            for i in range(n):
                if i%2==0:
                    if s[i]!="r":
                        r1+=1
                    if s[i]!="b":
                        b2+=1
                else:
                    if s[i]!="b":
                        b1+=1
                    if s[i]!="r":
                        r2+=1
            print(min(max(r1,b1),max(r2,b2)))


obj=solve()