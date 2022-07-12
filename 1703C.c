#include<stdio.h>
#include<stdlib.h>
int main(){
    int t,*a,n,i,j,*d;
    char arr[100][10];
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a=(int*)malloc(n*sizeof(int));
        d=(int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        for(i=0;i<n;i++){
            scanf("%d",&d[i]);
            scanf("%s",&arr[i]);
            for(j=0;j<d[i];j++){
                if(arr[i][j]=='U'){
                    if(a[i]==0)
                    a[i]=9;
                    else
                    a[i]--;
                }
                else{
                    if(a[i]==9)
                    a[i]=0;
                    else
                    a[i]++;
                }
            }
        }
        for(i=0;i<n;i++)
        printf("%d ",a[i]);
        printf("\n");
        t--;
    }
}