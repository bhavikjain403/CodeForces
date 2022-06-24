from sys import stdin
def input(): return stdin.readline().strip()

t = int(input())
for case_num in range(t):
    input()
    s = [input() for _ in range(8)]
    found = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if s[i][j] == s[i - 1][j - 1] == s[i - 1][j + 1] == s[i + 1][j - 1] == s[i + 1][j + 1] == '#':
                print(i + 1, j + 1)
                found = 1
                break
        if found:
            break