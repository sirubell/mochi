#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
    int x, y;
    scanf("%d%d", &x, &y);
    int a = x / 1000, b = (x % 1000) / 100, c = (x % 100) / 10, d = (x % 10);
    int e = y / 1000, f = (y % 1000) / 100, g = (y % 100) / 10, h = (y % 10);
    int A = 0, B = 0;
    if (a == e)     A++;
    if (b == f)     A++;
    if (c == g)     A++;
    if (d == h)     A++;
    if ((e == b) || (e == c) || (e == d))   B++;
    if ((f == a) || (f == c) || (f == d))   B++;
    if ((g == b) || (g == a) || (g == d))   B++;
    if ((h == b) || (h == c) || (h == a))   B++;
    printf("%dA%dB", A, B);
}