t = int(input())
while t:
    s = input()
    if((s[0]=='y' or s[0]=='Y') and (s[1]=='e' or s[1]=='E') and (s[2]=='s' or s[2]=='S')):
        print("YES")
    else:
        print("NO")
    t-=1