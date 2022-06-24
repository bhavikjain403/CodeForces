#include<stdio.h>
#include<limits.h>

int findmax(int a, int b){
    if(a>b)
    return a;
    return b;
}

int main(){
    int t, n, m, a[40][40], i, j, x, y, p;
    scanf("%d",&t);
    while(t){
        scanf("%d %d",&n,&m);
        p=-INT_MAX;
        for(i=0; i<n; i++)
        {
            for(j=0; j<m; j++)
            {
                scanf("%d",&a[i][j]);
                if(a[i][j]>p)
                {
                    p=a[i][j];
                    x=i;
                    y=j;
                }
            }
        }
        printf("%d\n",findmax(n-x,x+1)*findmax(m-y,y+1));
        t--;
    }
    return 0;
}