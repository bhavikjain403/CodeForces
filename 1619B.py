t=int(input())
while t:
    n=int(input())
    s=set()
    i=1
    while i*i<=n:
        s.add(i*i)
        i+=1
    i=1
    while i*i*i<=n:
        s.add(i*i*i)
        i+=1
    print(len(s))
    t-=1