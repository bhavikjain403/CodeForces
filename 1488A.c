#include<stdio.h>
#include<math.h>
int main(){
    int t,x,y,k,q,c;
    scanf("%d",&t);
    while(t)
    {
        scanf("%d %d",&x,&y);
        if(x>y)
        printf("%d\n",y);
        else if(x==y)
        printf("1\n");
        else{
            k=0;
            q=(int)log10(y/x);
            c=0;
            while(q+1){
            while(k+x*pow(10,q)<=y){
                k+=x*pow(10,q);
                c++;
            }
            q--;
            }
            printf("%d\n",c+y-k);
        }
        t--;
    }
    return 0;
}