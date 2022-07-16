#include<stdio.h>
#include<stdlib.h>
int main(){
    int i,t,n,*a,flag,p0,p1;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a = (int*)malloc(n*sizeof(int));
        scanf("%d%d",&a[0],&a[1]);
        if(n==2)
        printf("YES\n");
        else{
            flag=1;
            p0=a[0]%2;
            p1=a[1]%2;
            for(i=2;i<n;i++){
                scanf("%d",&a[i]);
                if(flag==1){
                    if(i%2==0 && a[i]%2!=p0)
                    flag=0;
                    else if(i%2==1 && a[i]%2!=p1)
                    flag=0;
                }
            }
            if(flag)
            printf("YES\n");
            else
            printf("NO\n");
        }
        t--;
    }
    return 0;
}