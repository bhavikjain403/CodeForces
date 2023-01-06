class solve:
    def __init__(self):
        n=int(input())
        d={}
        for i in range(n):
            name=input()
            if name not in d:
                d[name]=0
            else:
                d[name]+=1
            if d[name]==0:
                print("OK")
            else:
                print(name+str(d[name]))
 
obj=solve()