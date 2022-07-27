t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    for i in a:
        if i not in ans:
            ans.append(i)
    print(*ans)
    t-=1