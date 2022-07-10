t = int(input())
while t:
    s = input()
    lens = len(s)
    if lens<=3:
        print(1)
    else:
        day=0
        i=0
        while i<lens:
            a = s[i]
            lent = 1
            while i+1<lens and lent<3:
                if s[i+1] not in a:
                    a+=s[i+1]
                    lent+=1
                i+=1
            day+=1
            if i==lens-1:
                break
            else:
                while i<lens and (s[i] in a):
                    i+=1
        print(day)
    t-=1