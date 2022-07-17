#include<stdio.h>
int main(){
    int t,n;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        printf("1 %d 1 1\n",n-3);
        t--;
    }
    return 0;
}