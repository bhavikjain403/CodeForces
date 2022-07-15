t = int(input())
while t:
    s = input()
    n = 0
    m = ord(s[0])
    score = 0
    idx = 0
    for i in s:
        score+=ord(i)-96
        n+=1
        if m>ord(i):
            m = ord(i)
            idx = n-1
    if n==1:
        print("Bob",score)
    elif n%2==0:
        print("Alice",score)
    elif idx==0 or idx==n-1:
        print("Alice",score-2*(m-96))
    else:
        m = min(ord(s[0])-96,ord(s[-1])-96)
        print("Alice",score-2*m)
    t-=1