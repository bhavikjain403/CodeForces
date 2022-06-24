#include<stdio.h>
#include<stdlib.h>
int main(){
    int t, n, m, *a, i, s;
    scanf("%d",&t);
    while(t){
        scanf("%d %d",&n,&m);
        s=0;
        a=(int*)malloc(sizeof(int)*n);
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            s+=a[i];
        }
        if(m>=s)
        printf("0\n");
        else
        printf("%d\n",s-m);
        t--;
    }
    return 0;
}