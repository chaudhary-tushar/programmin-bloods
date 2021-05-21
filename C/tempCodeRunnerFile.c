#include<stdio.h>
#include<math.h>
int main()
{
    float A,I,P,R,n,t;
    printf("Enter the values of principal, rate of interest ,n and time");
    scanf("%f%f%f%f",&P,&R,&n,&t);
    A=P*((1+(R/(100*n))*(n*t)));
    I=A-P;
    printf("compound interest is %f and total amount is %f",I,A);
    return 0;
}