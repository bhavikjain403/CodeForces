t = int(input())
while t:
    n = int(input())
    a = set(map(int, input().split()))
    lena = len(a)
    ans = [lena]*lena
    j = lena
    for i in range(lena,n):
        j+=1
        ans.append(j)
    print(*ans)
    t-=1