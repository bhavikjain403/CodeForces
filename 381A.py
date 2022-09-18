n=int(input())
l=list(map(int,input().split()))
s,d=0,0
for i in range(n):
    if i%2:
        if l[0]>l[-1]:
            d+=l.pop(0)
        else:
            d+=l.pop(-1)
    else:
        if l[0]>l[-1]:
            s+=l.pop(0)
        else:
            s+=l.pop(-1)
print(s,d)