#include<stdio.h>
int main(){
    long long int p,a,b,c,l1,l2,l3;
    int t;
    scanf("%d",&t);
    while(t)
    {
        scanf("%lld %lld %lld %lld",&p,&a,&b,&c);
        if(p>a){
            if(p%a==0){
                l1=0;
            }
            else
            l1=a*(p/a+1)-p;
        }else l1=a-p;
        if(p>b){
            if(p%b==0){
                l2=0;
            }
            else
            l2=b*(p/b+1)-p;
        }else l2=b-p;
        if(p>c){
            if(p%c==0){
                l3=0;
            }
            else
            l3=c*(p/c+1)-p;
        }else l3=c-p;
        if(l1<l2){
            if(l1<l3)
            printf("%lld\n",l1);
            else
            printf("%lld\n",l3);
        }
        else
        {
            if(l2<l3)
            printf("%lld\n",l2);
            else
            printf("%lld\n",l3);
        }
        t--;
    }
    return 0;
}