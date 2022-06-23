#include<stdio.h>
int main(){
    int t, a, b, c;
    scanf("%d",&t);
    while(t){
        scanf("%d %d %d",&a, &b, &c);
        if(2*b==a+c)
        printf("YES\n");
        else if(2*b<a+c)
        {
            if((a+c)%(2*b)==0)
            printf("YES\n");
            else
            printf("NO\n");
        }
        else
        {
            if((2*b-c)%a==0 || (2*b-a)%c==0)
            printf("YES\n");
            else
            printf("NO\n");
        }
        t--;
    }
    return 0;
}