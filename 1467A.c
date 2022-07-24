#include<stdio.h>
int main(){
    int t,n,i,a;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a=9;
        for(i=0;i<n;i++){
            if(i==0)
            printf("%d",a--);
            else
            printf("%d",a++);
            if(a==10)
            a=0;
        }
        printf("\n");
        t--;
    }
    return 0;
}