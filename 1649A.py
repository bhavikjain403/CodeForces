t=int(input())
while t:
    n=int(input())
    a=list(map(int, input().split()))
    l=0
    r=n-1
    while l<n-1 and a[l+1]==1:
        l+=1
    while r>0 and a[r-1]==1:
        r-=1
    if r>l:
        print(r-l)
    else:
        print("0")
    t-=1