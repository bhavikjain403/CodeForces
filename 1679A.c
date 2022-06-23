#include<stdio.h>

void solve(long long int n)
{
    long long int min, max;
    if(n%2!=0 || n<=2){
        printf("-1\n");
        return;
    }
    else{
        n=n/2;
        if(n%3==0)
        min=n/3;
        else
        min=n/3+1;
        printf("%lld %lld\n",min,n/2);
    }
}

int main(){
    long long int t,n,min,max;
    scanf("%lld",&t);
    while (t)
    {
        scanf("%lld",&n);
        solve(n);
        t--;
    }
    return 0;
}