t = int(input())
while t:
    s = input()
    a = ord(s[0])
    b = ord(s[1])
    i=25*(a-96)
    if(b>a):
        i+=b-122
    else:
        i+=b-121
    print(i)
    t-=1