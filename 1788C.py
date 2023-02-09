class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        if n%2==0:
            print("No")
        else:
            print("Yes")
            if n==1:
                print("1 2")
                return
            for i in range(n//2+1):
                print(f"{2*i+1} {2*n-i}")
            for i in range(n//2):
                print(f"{2*i+2} {2*n-n//2-i-1}")

obj=solve()