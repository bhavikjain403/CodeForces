#include<stdio.h>
int main(){
    int t,l1,r1,l2,r2;
    scanf("%d",&t);
    while(t){
        scanf("%d%d%d%d",&l1,&r1,&l2,&r2);
        if(r1>=l2 && l1<=l2)
        printf("%d\n",l2);
        else if(r2>=l1 && l2<=l1)
        printf("%d\n",l1);
        else
        printf("%d\n",l2+l1);
        t--;
    }
}