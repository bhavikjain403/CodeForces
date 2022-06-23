n = int(input())
while n:
    s = input()
    t = len(s)
    if t>10:
        print(f"{s[0]}{t-2}{s[-1]}")
    else:
        print(s)
    n-=1