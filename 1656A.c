#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
int main(){
    int t,n,min,max,*a,i,x,y;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        min=INT_MAX;
        max=INT_MIN;
        a=(int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(min>a[i]){
                x=i+1;
                min=a[i];
            }
            if(max<a[i]){
                y=i+1;
                max=a[i];
            }
        }
        printf("%d %d\n",x,y);
        t--;
    }
    return 0;
}