#include<stdio.h>
void findmax(int a, int b){
    if(a>b)
    printf("%d\n",a);
    else
    printf("%d\n",b);
}


int main(){
    int t, l, r, a;
    scanf("%d",&t);
    while(t){
        scanf("%d %d %d",&l, &r, &a);
        if(l/a==r/a)
        printf("%d\n",r/a+r%a);
        else
        findmax(r/a+r%a, r/a-1 + a-1);
        t--;
    }
    return 0;
}