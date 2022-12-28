from collections import Counter

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        c=Counter(s).most_common()[0][0]
        if c=="R":
            ans="P"
        elif c=="S":
            ans="R"
        else:
            ans="S"
        print(ans*len(s))

obj=solve()