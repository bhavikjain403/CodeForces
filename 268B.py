n=int(input())
if n==1:
    print("1")
elif n==2:
    print("3")
else:
    ans=n
    for i in range(1,n):
        ans+=(n-i)*(i+1)-i
    print(ans)