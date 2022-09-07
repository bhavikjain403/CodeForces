def isprime(m):
    if m%2:
        for i in range(2,m//2+1):
            if m%i==0:
                return False
        return True
    return False

n,m=map(int,input().split())
if isprime(m):
    flag=1
    for i in range(n+1,m+1):
        if i!=m and isprime(i):
            flag=0
            print("NO")
            break
    if flag:
        print("YES")
else:
    print("NO")