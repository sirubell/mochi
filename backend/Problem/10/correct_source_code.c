#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
 
int main()
{
    int number;
    int x1, y1, x2, y2, x3, y3;
    scanf("%d", &number);
    while (number > 0) {
        scanf("%d%d%d%d%d%d", &x1, &y1, &x2, &y2, &x3, &y3);
        int a, b, c;
        a = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        b = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2);
        c = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3);
        if ((a == b) || (b == c) || (a == c))
            printf("isosceles\n");
        else if ((a + b == c) || (b + c == a) || (a + c == b))
            printf("right\n");
        else if (a > b && a > c) {
            if ((x2 - x3) * (x1 - x3) + (y2 - y3) * (y1 - y3) > 0)
                printf("acute\n");
            else
                printf("obtuse\n");
        }
        else if (b > a && b > c) {
            if ((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) > 0)
                printf("acute\n");
            else
                printf("obtuse\n");
        }
        else if (c > a && c > b) {
            if ((x1 - x2) *(x3 - x2) + (y1 - y2) * (y3 - y2) > 0)
                printf("acute\n");
            else
                printf("obtuse\n");
        }
        number--;
    }
}