class SegmentTree:
    def buildSegTree(self,arr,seg,idx,low,high,c):
        if low==high:
            seg[idx]=arr[low]
            return
        mid=(low+high)//2
        self.buildSegTree(arr,seg,2*idx+1,low,mid,not c)
        self.buildSegTree(arr,seg,2*idx+2,mid+1,high,not c)
        if c:
            seg[idx]=seg[2*idx+1]|seg[2*idx+2]
        else:
            seg[idx]=seg[2*idx+1]^seg[2*idx+2]    

    def updateQuery(self,seg,low,high,idx,i,val,c):
        if low==high:
            seg[idx]=val
            return
        mid=(low+high)//2
        if i<=mid:
            self.updateQuery(seg,low,mid,2*idx+1,i,val,not c)
        else:
            self.updateQuery(seg,mid+1,high,2*idx+2,i,val,not c)
        if c:
            seg[idx]=seg[2*idx+1]|seg[2*idx+2]
        else:
            seg[idx]=seg[2*idx+1]^seg[2*idx+2]

n,m=map(int,input().split())
a=list(map(int,input().split()))
l=2**n
seg=[0]*(4*l)
tree = SegmentTree()
tree.buildSegTree(a,seg,0,0,l-1,n%2)
for i in range(m):
    pos,val=map(int,input().split())
    pos-=1
    tree.updateQuery(seg,0,l-1,0,pos,val,n%2)
    print(seg[0])