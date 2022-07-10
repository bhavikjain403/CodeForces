t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = sum(map(int, input().split()))
    print(a[b%n])
    t-=1