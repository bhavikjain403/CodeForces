#include<stdio.h>

void solve(int a,int b,int c,int x,int y){
    if(a+c>=x){
        if(a<x)
        c=c-(x-a);
        if(b+c>=y){
            printf("YES\n");
            return;
        }
        else{
            printf("NO\n");
            return;
        }
    }
    else{
        printf("NO\n");
    }
}

int main(){
    int a,b,c,x,y,t;
    scanf("%d",&t);
    while(t)
    {
        scanf("%d%d%d%d%d",&a,&b,&c,&x,&y);
        solve(a,b,c,x,y);
        t--;
    }
    return 0;
}