#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,n,*a,i,m;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a=(int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        i=1;
        m=0;
        while(i<n-1){
            if(a[i]>a[i-1] && a[i]>a[i+1]){
                m+=1;
                if(i+2<=n-1){
                    if(a[i+2]>=a[i])
                    a[i+1]=a[i+2];
                    else
                    a[i+1]=a[i];
                }
                else
                a[i+1]=a[i];
                i+=2;
            }
            else
            i+=1;
        }
        printf("%d\n",m);
        for(i=0;i<n;i++)
        printf("%d ",a[i]);
        printf("\n");
        t--;
    }
    return 0;
}