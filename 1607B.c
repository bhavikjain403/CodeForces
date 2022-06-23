#include<stdio.h>
int main(){
    int t;
    long long int x,n,r;
    scanf("%d",&t);
    while (t)
    {
        scanf("%lld %lld",&x,&n);
        if(n%4==0)
        printf("%lld\n",x);
        else
        {
            r=n%4;
            while (r)
            {
                if(x%2==0)
                x = x - (n-r+1);
                else
                x = x + n-r+1;
                r= r-1;
            }
            printf("%lld\n",x);
        }
        t--;
    }
    return 0;
}