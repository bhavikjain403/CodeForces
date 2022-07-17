#include<stdio.h>
int main(){
    int t,a,b;
    scanf("%d",&t);
    while(t){
        scanf("%d%d",&a,&b);
        if(a==0)
        printf("1\n");
        else
        printf("%d\n",a+1+b*2);
        t--;
    }
    return 0;
}