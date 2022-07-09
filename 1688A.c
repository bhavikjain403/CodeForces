#include<stdio.h>
int main(){
    int t,n,i;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        i=n&(-n);
        while(((i&n) <= 0) || ((i^n) <= 0)){
            i++;
        }
        printf("%d\n",i);
        t--;
    }
    return 0;
}