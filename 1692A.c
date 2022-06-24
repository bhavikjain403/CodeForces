#include<stdio.h>
int main(){
    int t,a,b,c,d,x;
    scanf("%d",&t);
    while(t){
        x=0;
        scanf("%d%d%d%d",&a,&b,&c,&d);
        if(a<b)
        x++;
        if(a<c)
        x++;
        if(a<d)
        x++;
        printf("%d\n",x);
        t--;
    }
}