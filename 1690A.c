#include<stdio.h>
int main(){
    int n,t,h1,h2,h3;
    scanf("%d",&t);
    while(t){
        h1=3;
        h2=2;
        h3=1;
        scanf("%d",&n);
        n=n-6;
        while(n){
            h1++;
            n--;
            if(n){
                h2++;
                n--;
            }
            if(n){
                h3++;
                n--;
            }
        }
        printf("%d %d %d\n",h2,h1,h3);
        t--;
    }
    return 0;
}