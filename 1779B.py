class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        if n==3:
            print("NO")
        elif n%2==0:
            print("YES")
            for i in range(n//2):
                print("1 -1 ",end="")
            print()
        else:
            print("YES")
            c=1+(n-5)//2
            d=-c-1
            for i in range(n//2):
                print(f"{c} {d} ",end="")
            print(c)
 
obj=solve()