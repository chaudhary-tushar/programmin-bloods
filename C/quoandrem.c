#include<stdio.h>
int main()
{
    int quo,rem,divisor,dividend;
    printf("give two integral inputs");
    scanf("%d%d",&dividend,&divisor);
    quo=dividend/divisor;
    rem=dividend%divisor;
    printf("quotient : %d and remainder: %d",quo,rem);
    return 0;
}