t = int(input())
while t:
    n,z=map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i]=a[i]|z
    print(max(a))
    t-=1