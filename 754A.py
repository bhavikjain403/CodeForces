class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        if a[0]==0 and len(set(a))==1:
            print("NO")
        else:
            print("YES")
            if sum(a)!=0:
                print("1")
                print(f"1 {n}")
            else:
                i=0
                while i<n:
                    if a[i]!=0:
                        break
                    i+=1
                print("2")
                print(f"1 {i+1}")
                print(f"{i+2} {n}")
 
obj=solve()