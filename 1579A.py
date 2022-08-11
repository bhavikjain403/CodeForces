t=int(input())
while t:
    s=input()
    if s.count("B")==s.count("A")+s.count("C"):
        print("YES")
    else:
        print("NO")
    t-=1