n=int(input())
a=list(map(int,input().split()))
ans=abs(a[0]-a[n-1])
i1,i2=1,n
for i in range(1,n):
    t=abs(a[i]-a[i-1])
    if ans>t:
        ans=t
        i1,i2=i,i+1
print(i2,i1)