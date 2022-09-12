t=int(input())
while t:
    n=int(input())
    s=input()
    ans=""
    i=n-1
    while i>=0:
        if s[i]=="0":
            ans+=chr(96+int(s[i-2]+s[i-1]))
            i-=3
        else:
            ans+=chr(96+int(s[i]))
            i-=1
    print(ans[::-1])
    t-=1