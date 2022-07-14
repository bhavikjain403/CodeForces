#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,n,min,*arr,i,count;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        arr = (int*)malloc(n*sizeof(int));
        scanf("%d",&arr[0]);
        min = arr[0];
        count=0;
        for(i=1;i<n;i++){
            scanf("%d",&arr[i]);
            if(min>arr[i])
            min=arr[i];
        }
        for(i=0;i<n;i++){
            count+=arr[i]-min;
        }
        printf("%d\n",count);
        t--;
    }
    return 0;
}