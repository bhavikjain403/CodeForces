class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        pos={}
        for i in range(n):
            pos[a[i]]=i
        d={}
        for i in range(n):
            temp=pos[b[i]]-i
            if temp<0:
                temp+=n
            if temp not in d:
                d[temp]=1
            else:
                d[temp]+=1
        print(max(d.values()))

obj=solve()