class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s1=input()
        s2=input()
        print(len(set(s1+s2))-1)
 
obj=solve()