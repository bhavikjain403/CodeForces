def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b%a, a)

t=int(input())
while t:
    count=0
    n=int(input())
    a=list(map(int,input().split()))
    e=list(filter(lambda x:x%2==0,a))
    o=list(filter(lambda x:x%2==1,a))
    e.sort(reverse=True)
    o.sort(reverse=True)
    a=e+o
    for i in range(n):
        for j in range(i+1,n):
            if gcd(a[i],2*a[j])>1:
                count+=1
    print(count)
    t-=1