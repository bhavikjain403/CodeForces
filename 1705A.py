def solve(n,x,l1,l2):
    for i in range(n):
        if l1[i]+x>l2[i]:
            print("NO")
            return
    print("YES")

t = int(input())
while t:
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    l1 = l[:n]
    l2 = l[n:2*n]
    solve(n,x,l1,l2)
    t-=1