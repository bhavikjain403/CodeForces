def solve(s,l):
    for i in range(1,l-1):
        if s[i]==s[i-1] or s[i]==s[i+1]:
            continue
        else:
            print("NO")
            return
    print("YES")

t = int(input())
while t:
    s = input()
    l = len(s)
    if l>1:
        if s[0]!=s[1] or s[-1]!=s[-2]:
            print("NO")
        else:
            solve(s,l)
    else:
        print("NO")
    t-=1