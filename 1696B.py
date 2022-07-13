def solve(n,l):
    z = 0
    left = -1
    right = n-1
    for i in range(n):
        if l[i]==0:
            z+=1
        else:
            if(left==-1):
                left = i
            right = i
    if(z==n):
        print("0")
        return
    if(z==0):
        print("1")
        return
    allZero = 1
    for i in range(left):
        if l[i]!=0:
            print("2")
            return
    for i in range(right+1,n):
        if l[i]!=0:
            print("2")
            return
    for i in range(left,right+1):
        if l[i]==0:
            print("2")
            return
    print("1")

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    solve(n,l)
    t-=1