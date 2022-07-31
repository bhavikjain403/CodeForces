t=int(input())
while t:
    n=int(input())
    s=input()
    if n>2:
        print("NO")
    elif n==1:
        print("YES")
    else:
        if s[0]==s[1]:
            print("NO")
        else:
            print("YES")
    t-=1