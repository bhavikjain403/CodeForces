#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,n,*s,*f,i,*d,time;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        s=(int*)malloc(n*sizeof(int));
        f=(int*)malloc(n*sizeof(int));
        d=(int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++)
        scanf("%d",&s[i]);
        for(i=0;i<n;i++)
        scanf("%d",&f[i]);
        time=s[0];
        for(i=0;i<n;i++){
            if(time>s[i])
                d[i]=f[i]-time;
            else
                d[i]=f[i]-s[i];
            time=f[i];
            printf("%d ",d[i]);
        }
        printf("\n");
        t--;
    }
    return 0;
}