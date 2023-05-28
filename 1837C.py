class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=list(input())
        temp='0'
        for i in range(len(s)):
            if s[i]=='?':
                s[i]=temp
            temp=s[i]
        print("".join(s))
    
obj=solve()