#include<stdio.h>
#include<stdlib.h>
int main(){
    int *a,*b,n,m,t,i,maxa,maxb;
    scanf("%d",&t);
    while(t){
        scanf("%d",&n);
        a=(int*)malloc(sizeof(int)*n);
        scanf("%d",&a[0]);
        maxa=a[0];
        for(i=1;i<n;i++){
            scanf("%d",&a[i]);
            if(maxa<a[i]) maxa=a[i];
        }
        scanf("%d",&m);
        b=(int*)malloc(sizeof(int)*m);
        scanf("%d",&b[0]);
        maxb=b[0];
        for(i=1;i<m;i++){
            scanf("%d",&b[i]);
            if(maxb<b[i]) maxb=b[i];
        }
        if(maxa==maxb) printf("Alice\nBob\n");
        else if(maxa>maxb) printf("Alice\nAlice\n");
        else printf("Bob\nBob\n");
        t--;
    }
}