class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        se,so=(k-1)*2,k-1
        if (n-se)%2==0 and n-se>0:
            print("YES")
            for i in range(k-1):
                print("2",end=" ")
            print(n-se)
        elif (n-so)%2 and n-so>0:
            print("YES")
            for i in range(k-1):
                print("1",end=" ")
            print(n-so)
        else:
            print("NO")
 
obj=solve()