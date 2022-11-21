class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        s=input()
        ans=0
        for i in s:
            ans=max(ans,ord(i)-96)
        print(ans)

obj=solve()