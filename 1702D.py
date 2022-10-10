from collections import defaultdict

t=int(input())
while t:
    w=input()
    p=int(input())
    sw=sorted(w,reverse=True)
    cost=0
    for i in w:
        cost+=ord(i)-96
    d=defaultdict(int)
    for i in range(len(sw)):
        if cost>p:
            d[sw[i]]+=1
            cost-=(ord(sw[i])-96)
    for i in range(len(w)):
        if d[w[i]]>0:
            d[w[i]]-=1
            continue
        print(w[i],end="",sep="")
    print()
    t-=1