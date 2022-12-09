class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print(f"1 {a[0]} 0")
            return
        if n==2:
            print(f"2 {a[0]} {a[1]}")
            return
        i,j=0,n-1
        al,bo=0,0
        alt,bot=0,0
        turn=0
        c=0
        while i<=j:
            if turn==0:
                turn=1
                al=0
                while al<=bo and i<=j:
                    al+=a[i]
                    i+=1
                alt+=al
            else:
                turn=0
                bo=0
                while bo<=al and j>=i:
                    bo+=a[j]
                    j-=1
                bot+=bo
            c+=1
        print(c,alt,bot)

obj=solve()