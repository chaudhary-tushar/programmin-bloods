#include<stdio.h>
#include<math.h>
int main()
{
    int x1,x2,y1,y2;
    float d;
    printf("Enter the coordinates x1:y1,x2:y2 respectively");
    scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
    d=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
    printf("the distance between the points is %f",d);
    return 0;


}