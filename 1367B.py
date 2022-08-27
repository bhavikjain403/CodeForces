t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().split()))
    e,o=0,0
    for i in l:
        if i%2==0:
            e+=1
        else:
            o+=1
    if n%2==0 and e!=o:
        print("-1")
    elif n%2==1 and e!=o+1:
        print("-1")
    else:
        ans=0
        for i in range(n):
            if i%2!=l[i]%2:
                ans+=1
        print(ans//2)
    t-=1