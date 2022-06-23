#include<stdio.h>
void solve(int l[], int n){
    int c=0,i;
    for(i=n-2;i>=0;i--){
        while (l[i]>=l[i+1] && l[i]>0)
        {
            l[i]/=2;
            c++;
        }
        if (l[i]==l[i+1])
        {
            printf("%d\n",-1);
            return;
        }
    }
    printf("%d\n",c);
}

int main(){
    int n,l[31],t,i;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%d",&l[i]);
        solve(l,n);
        t--;
    }
    return 0;
}