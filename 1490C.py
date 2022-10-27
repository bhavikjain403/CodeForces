import math

t=int(input())
while t:
    n=int(input())
    flag,i=1,1
    while i**3<n:
        temp=(n-i**3)**(1/3)
        if math.ceil(temp)-temp<=0.0000000001:
            print("YES")
            flag=0
            break
        i+=1
    if flag:
        print("NO")
    t-=1