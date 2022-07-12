def cost(a,b,m):
    value = 0
    for i in range(m):
        value+=abs(ord(a[i])-ord(b[i]))
    return value

t = int(input())
while t:
    n,m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(input())
    count = 99999999
    for i in range(n):
        for j in range(i+1,n):
            count=min(count, cost(l[i],l[j],m))
    print(count)
    t-=1