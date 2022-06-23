t = int(input())
while t:
    n = int(input())
    need = 0
    have = 0
    ans = 1
    a = list(map(int, input().split()))
    for j in range(n):
        need += j
        have += a[j]
        if have < need:
            ans = 0
    if ans:
        print("YES")
    else:
        print("NO")
    t-=1