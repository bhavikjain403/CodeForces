class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        if n==1:
            print("1")
            print("1 2")
        else:
            print(n//2+n%2)
            for i in range(n//2):
                print(i*3+1,(n-i)*3)
            if n%2:
                print(((n*3)//2),((n*3)//2+2))

obj=solve()