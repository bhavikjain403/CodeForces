#include<stdio.h>
int main(){
    int t,x,y;
    scanf("%d",&t);
    while (t)
    {
        scanf("%d%d",&x,&y);
        if(y%x==0)
        printf("%d %d\n",1,y/x);
        else
        printf("%d %d\n",0,0);
        t--;
    }
    return 0;
}