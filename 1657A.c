#include<stdio.h>
#include<math.h>
int main(){
    int x,y,t;
    float d;
    scanf("%d",&t);
    while(t){
        scanf("%d%d",&x,&y);
        if(x==0 && y==0)
        printf("0\n");
        else{
            d=pow(x*x+y*y,0.5);
            if(d==(int)d)
            printf("1\n");
            else
            printf("2\n");
        }
        t--;
    }
    return 0;
}