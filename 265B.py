n=int(input())
h=0
ans=2*n-1
for i in range(n):
    temp=int(input())
    ans+=abs(temp-h)
    h=temp
print(ans)