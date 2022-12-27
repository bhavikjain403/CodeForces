class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        if n%4:
            print("NO")
        else:
            print("YES")
            se,so=0,0
            for i in range(n//2):
                print((i+1)*2,end=" ")
                se+=(i+1)*2
            for i in range(n//2-1):
                print(i*2+1,end=" ")
                so+=i*2+1
            print(se-so)
 
obj=solve()