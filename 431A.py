from collections import Counter

a1,a2,a3,a4=map(int,input().split())
s=input()
c=Counter(s)
print(c["1"]*a1+c["2"]*a2+c["3"]*a3+c["4"]*a4)