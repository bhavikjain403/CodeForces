t=int(input())
while t:
    n=int(input())
    if n>=1900:
        print("Division 1")
    elif n>=1600 and n<1900:
        print("Division 2")
    elif n>=1400 and n<1600:
        print("Division 3")
    else:
        print("Division 4")
    t-=1