#include<stdio.h>
int main(){
    long long int t,n,s;
    scanf("%lld",&t);
    while(t){
        scanf("%lld%lld",&n,&s);
        printf("%lld\n",s/(n*n));
        t--;
    }
    return 0;
}