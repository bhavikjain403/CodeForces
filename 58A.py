s=input()
ih,ie,il1,il2,io=-1,-1,-1,-1,-1
for i in range(len(s)):
    if s[i]=="h":
        ih=i
        break
if ih!=-1:
    s=s[ih:]
    for i in range(len(s)):
        if s[i]=="e":
            ie=i
            break
    if ie!=-1:
        s=s[ie:]
        for i in range(len(s)):
            if s[i]=="l":
                il1=i
                break
        if il1!=-1:
            s=s[il1:]
            l=len(s)
            if l!=1:
                for i in range(1,l):
                    if s[i]=="l":
                        il2=i
                        break
                if il2!=-1:
                    s=s[il2:]
                    for i in range(len(s)):
                        if s[i]=="o":
                            io=i
                            break
                    if io!=-1:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")