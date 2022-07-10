from math import log10
t = int(input())
while t:
    n = int(input())
    print(n-10**(int)(log10(n)))
    t-=1