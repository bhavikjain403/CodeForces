t=int(input())
while t:
    s=input()
    n=len(s)
    d=dict()
    for i in s:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for i in range(n):
        d[s[i]]-=1
        if d[s[i]]==0:
            print(s[i:])
            break
    t-=1