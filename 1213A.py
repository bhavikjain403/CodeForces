class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        e,o=0,0
        for i in a:
            if i%2:
                o+=1
            else:
                e+=1
        print(min(e,o))
 
obj=solve()