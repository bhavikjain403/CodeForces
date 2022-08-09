t=int(input())
while t:
    n=input()
    if int(n[-1])%2==1:
        if int(n[0])%2==0:
            print("1")
        else:
            flag=0
            for i in n:
                if int(i)%2==0:
                    flag=1
                    break
            if flag:
                print("2")
            else:
                print("-1")
    else:
        print("0")
    t-=1