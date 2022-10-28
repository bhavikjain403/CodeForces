t=int(input())
while t:
    num=input()
    x = [ord(c) - ord('0') for c in num]
    n = len(x)
    for i in range(n - 2, -1, -1):
        if x[i] + x[i + 1] >= 10:
            x[i + 1] += x[i] - 10
            x[i] = 1
            break
    else:
        x[1] += x[0]
        x.pop(0)
    print(''.join([chr(c + ord('0')) for c in x]))
    t-=1