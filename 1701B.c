#include<stdio.h>
#include<stdlib.h>
int main(){
    int t, n, i, j;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        printf("2\n");
        for(i=1;i<=n;i++){
            if(i%2!=0){
                for(j=i;j<=n;j*=2){
                    printf("%d ",j);
                }
            }
        }
        printf("\n");
        t--;
    }
    return 0;
}