class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        a = set(map(int, input().split()))
        ans = 0
        for i in range(10000):
            num = str(i)
            num = (4 - len(num)) * '0' + num
            used = set(num)
            if len(used) != 2:
                continue
            d1 = int(used.pop())
            d2 = int(used.pop())
            if (not d1 in a) and (not d2 in a) and num.count(num[0]) == 2:
                ans += 1
        print(ans)
 
obj=solve()