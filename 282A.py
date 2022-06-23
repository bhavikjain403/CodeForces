n = int(input())
x = 0
while n:
    s = input()
    if s.count('+'):
        x+=1
    elif s.count('-'):
        x-=1
    n-=1
print(x)