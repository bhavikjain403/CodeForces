class solve:
    def solve(self,seq,a,b):
        i,j=seq.find(a),seq.rfind(b)
        return i!=-1 and j!=-1 and i+len(a)<=j

    def __init__(self):
        seq=input()
        a=input()
        b=input()
        print(['fantasy', 'backward', 'forward', 'both'][2*self.solve(seq,a,b)+self.solve(seq[::-1],a,b)])
 
obj=solve()