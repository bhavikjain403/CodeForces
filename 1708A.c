#include<stdio.h>
#include<stdlib.h>
int main(){
    int i,t,n,*a,flag,r,q;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a = (int*)malloc(n*sizeof(int));
        flag=1;
        scanf("%d",&a[0]);
        for(i=1;i<n;i++){
            scanf("%d",&a[i]);
            if(flag==1){
            q = a[i]/a[i-1];
            r = a[i]%a[i-1];
            if(r==0)
            a[i]-=a[i-1]*(q-1);
            else
            a[i]-=a[i-1]*q;
            if(a[i]<a[i-1])
            flag=0;}
        }
        if(flag)
        printf("YES\n");
        else
        printf("NO\n");
        t--;
    }
    return 0;
}