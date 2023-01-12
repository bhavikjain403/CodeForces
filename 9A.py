class solve:
    def __init__(self):
        y,w=map(int,input().split())
        data=["", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"]
        print(data[max(y,w)])
 
obj=solve()