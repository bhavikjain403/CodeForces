#include<stdio.h>
int main(){
    int t;
    long long int n,ans,q,r;
    scanf("%d",&t);
    while(t){
        scanf("%lld",&n);
        q=n/6;
        r=n%6;
        if(n<=6)
        ans=15;
        else if(r==0)
        ans=q*15;
        else if(r<=2)
        ans=q*15+5;
        else if(r<=4)
        ans=q*15+10;
        else
        ans=(q+1)*15;
        printf("%lld\n",ans);
        t--;
    }
    return 0;
}