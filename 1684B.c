#include<stdio.h>
int main(){
    int t,a,b,c;
    scanf("%d",&t);
    while(t){
        scanf("%d%d%d",&a,&b,&c);
        printf("%d %d %d\n",a+b+c,b+c,c);
        t--;
    }
    return 0;
}