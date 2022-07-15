def solve(n,l):
    i5 = -1
    i0 = -1
    for i in range(l-1,-1,-1):
        if n[i]=="5":
            i5=i
            break
    for i in range(l-1,-1,-1):
        if n[i]=="0":
            i0=i
            break
    if i5!=-1:
        count5=l-1-i5
        for i in range(i5-1,-1,-1):
            if n[i]=="2" or n[i]=="7":
                break
            count5+=1
    if i0!=-1:
        count0=l-1-i0
        for i in range(i0-1,-1,-1):
            if n[i]=="0" or n[i]=="5":
                break
            count0+=1
    if i0==-1:
        print(count5)
    elif i5==-1:
        print(count0)
    else:
        print(min(count0,count5))

t = int(input())
while t:
    n = input()
    num = int(n)
    if(num%25==0):
        print("0")
    else:
        l = len(n)
        solve(n,l)
    t-=1