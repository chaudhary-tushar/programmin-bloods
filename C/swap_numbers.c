#include<stdio.h>
int main()
{
    int a,b,temp;
    printf("give two numbers to be swapped");
    scanf("%d%d",&a,&b);
    temp=a;
    a=b;
    b=temp;
    printf("the two numbers are %d %d",a,b);
    return 0;

}