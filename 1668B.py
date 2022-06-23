t = int(input())
while t:
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    if n>m:
        print("NO")
    else:
        l.sort()
        s = n + sum(l) - l[0] + l[-1]
        if m<s:
            print("NO")
        else:
            print("YES")
    t-=1