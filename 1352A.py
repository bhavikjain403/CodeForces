t=int(input())
while t:
    n=int(input())
    ans=[]
    prod=[]
    val=1
    while n:
        if n%10:
            ans.append(n%10)
            prod.append(val)
        val*=10
        n=n//10
    l=len(ans)
    for j in range(l):
        ans[j]*=prod[j]
    print(l)
    print(*ans)
    t-=1