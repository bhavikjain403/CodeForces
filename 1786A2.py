class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        answer = [0, 0, 0, 0]
        first_card = 1
        for it in range(1, 20000):
            who = 0 if it % 4 == 1 or it % 4 == 0 else 1
            cnt = it
            if n < cnt:
                cnt = n
            cnt_white = (cnt + first_card % 2) // 2
            cnt_black = cnt - cnt_white
            answer[who * 2 + 0] += cnt_white
            answer[who * 2 + 1] += cnt_black
            first_card += cnt
            n -= cnt
            if n == 0:
                break
        print(*answer)
 
obj=solve()