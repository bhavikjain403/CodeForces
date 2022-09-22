n, k, l, c, d, p, nl, np=map(int,input().split())
ml=k*l
sl=c*d
print(min(ml//nl,sl,p//np)//n)