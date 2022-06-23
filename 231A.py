n = int(input())
c=0
while n:
    l = list(map(int,input().split()))
    one = l.count(1)
    if one>1:
        c+=1
    n-=1
print(c)