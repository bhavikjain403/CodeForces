x=int(input())
while x:
    s=input()
    t=input()
    lt=len(t)
    if lt==1 and t[0]=="a":
        print("1")
    elif ("a" in t) and ("a" in s):
        print("-1")
    else:
        c=s.count("a")
        if c:
            print(2**c)
        else:
            print("1")
    x-=1