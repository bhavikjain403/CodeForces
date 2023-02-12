class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m=map(int,input().split())
        grid=[]
        for i in range(n):
            grid.append(list(input()))
        for col in range(m):
            obs=n-1
            for row in range(n-1,-1,-1):
                if grid[row][col]=="o":
                    obs=row-1
                elif grid[row][col]=="*":
                    grid[row][col]="."
                    grid[obs][col]="*"
                    obs-=1
        for i in grid:
            print("".join(i))

obj=solve()