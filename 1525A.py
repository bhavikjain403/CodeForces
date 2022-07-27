from math import gcd

t=int(input())
while t:
    k=int(input())
    print(100//gcd(100,k))
    t-=1