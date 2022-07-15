#include<stdio.h>
#include<stdlib.h>
int main(){
    long long int n,*a,i,count,sum,zcount;
    int t;
    scanf("%d",&t);
    while(t){
        scanf("%lld",&n);
        a=(long long int*)malloc(n*sizeof(long long int));
        count = -1;
        sum=0;
        zcount=0;
        for(i=0;i<n;i++){
            scanf("%lld",&a[i]);
            sum+=a[i];
            if(count==-1 && a[i]!=0)
            count=i;
            if(a[i]==0)
            zcount++;
        }
        if(count==-1)
        printf("0\n");
        else{
            sum-=a[n-1];
            zcount-=count;
            if(a[n-1]==0)
            zcount-=1;
            printf("%lld\n",sum+zcount);
        }
        t--;
    }
    return 0;
}