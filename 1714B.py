t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    l=len(a)
    if l==len(set(a)):
        print("0")
    else:
        for i in range(l-2,-1,-1):
            temp=a[i+1:]
            if a[i] in temp:
                print(i+1)
                break
    t-=1