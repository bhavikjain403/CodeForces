#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,n,i,w,*a;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        w=0;
        a=(int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]!=1 && a[i]%2==0){
                if(w==0)
                w=1;
                else
                w=0;
            }
        }
        if(w==0)
        printf("maomao90\n");
        else
        printf("errorgorn\n");
        t--;
    }
}