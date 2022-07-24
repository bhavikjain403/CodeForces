#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,n,*a,i,o,e;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        if(n==1)
        printf("1\n");
        else{
            a=(int*)malloc(n*sizeof(int));
            if(n%2==0){
                o=1;
                e=2;
                for(i=0;i<n;i++){
                    if(i%2==0){
                        a[i]=e;
                        e+=2;
                    }
                    else{
                        a[i]=o;
                        o+=2;
                    }
                    printf("%d ",a[i]);
                }
            }
            else{
                o=3;
                e=2;
                for(i=0;i<n-1;i++){
                    if(i%2==0){
                        a[i]=e;
                        e+=2;
                    }
                    else{
                        a[i]=o;
                        o+=2;
                    }
                    printf("%d ",a[i]);
                }
                printf("1");
            }
            printf("\n");
        }
        t--;
    }
}