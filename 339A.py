s = input()
s = sorted(s)
ans=''
for i in range(len(s)):
    if s[i]=='+':
        continue
    else:
        s[i]+='+'
        ans+=s[i]
print(ans[:-1])