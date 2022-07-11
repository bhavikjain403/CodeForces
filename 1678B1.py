t = int(input())
while t:
    n = int(input())
    s = input()
    i=0
    c=0
    while i<n:
        if s[i]!=s[i+1]:
            c+=1
        i+=2
    print(c)
    t-=1