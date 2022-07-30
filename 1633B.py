t=int(input())
while t:
    s=input()
    o=s.count("1")
    z=s.count("0")
    if o+z<=2:
        print("0")
    else:
        if o==z:
            print(o-1)
        else:
            print(min(o,z))
    t-=1