t=int(input())
while t:
    n=int(input())
    s=input()
    flag=0
    for i in range(n-2):
        if s[i]!=s[i+1] and (s[i] in s[i+2:]):
            flag=1
            break
    if flag:
        print("NO")
    else:
        print("YES")
    t-=1