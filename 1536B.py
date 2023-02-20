class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        for i in range(26):
            if chr(i+97) not in s:
                print(chr(i+97))
                return
        for i in range(26):
            for j in range(26):
                text=chr(i+97)+chr(j+97)
                if text not in s:
                    print(text)
                    return
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    text=chr(i+97)+chr(j+97)+chr(k+97)
                    if text not in s:
                        print(text)
                        return

obj=solve()