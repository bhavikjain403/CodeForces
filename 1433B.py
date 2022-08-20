from stringprep import in_table_a1


t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    i1,i2=0,0
    for i in range(n):
        if a[i]==1:
            i1=i
            break
    for i in range(n-1,-1,-1):
        if a[i]==1:
            i2=i
            break
    print(a[i1+1:i2].count(0))
    t-=1