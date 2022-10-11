t=int(input())
while t:
    a,b=map(str,input().split())
    a=sorted(a)
    b=sorted(b)
    la,lb=len(a),len(b)
    if a[0]=="S" and b[0]=="S":
        if la==lb:
            print("=")
        elif la>lb:
            print("<")
        else:
            print(">")
    elif a[0]=="S":
        print("<")
    elif b[0]=="S":
        print(">")
    elif a[0]=="M" and b[0]=="M":
        print("=")
    elif a[0]=="M" and b[0]=="L":
        print("<")
    elif a[0]=="L" and b[0]=="M":
        print(">")
    elif a[0]=="L" and b[0]=="L":
        if la==lb:
            print("=")
        elif la>lb:
            print(">")
        else:
            print("<")
    t-=1