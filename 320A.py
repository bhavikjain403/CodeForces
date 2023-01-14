class solve:
    def __init__(self):
        s=input()
        if s[0]!="1":
            print("NO")
        elif "444" in s:
            print("NO")
        else:
            flag=1
            for i in s:
                if i=="1" or i=="4":
                    continue
                else:
                    print("NO")
                    flag=0
                    break
            if flag:
                print("YES")
 
obj=solve()