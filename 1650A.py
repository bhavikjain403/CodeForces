t=int(input())
while t:
    s=input()
    c=input()
    n=len(s)
    if s[n-1]==c:
        print("YES")
    else:
        flag=0
        for i in range(n-2):
            if s[i]==c:
                a=len(s[:i])
                if a%2==0:
                    flag=1
                    print("YES")
                    break
        if flag==0:
            print("NO")
    t-=1