#include<stdio.h>
int main(){
    int t,n;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        if(n==1)
        printf("2\n");
        else if(n<=3)
        printf("1\n");
        else if(n%3==0)
        printf("%d\n",n/3);
        else
        printf("%d\n",n/3+1);
        t--;
    }
    return 0;
}