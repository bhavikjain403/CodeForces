#include<stdio.h>
#include<stdlib.h>

int findmin(int a,int b)
{
    if(a<b) return a;
    return b;
}

int main(){
    int t, n, *a, i, e, o;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a = (int*)malloc(n*sizeof(int));
        e=0;
        o=0;
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]%2==0) e++;
            else o++;
        }
        printf("%d\n", findmin(o,e));
        t--;
    }
}