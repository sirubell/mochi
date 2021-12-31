#include <stdio.h>
#include <stdlib.h>
 
int cmp(const void *a, const void *b)
{
    int flag = *(int *)a - *(int *)b;
    if (flag > 0) return 1;
    if (flag < 0) return -1;
    return 0;
}
 
int DFS(int *arr, int n, int now)
{
    if (now == 0) return 1;
    if (now < 0 || n <= 0) return 0;
    if (now < arr[n - 1]) return DFS(arr, n - 1, now);
    return DFS(arr, n - 1, now - arr[n - 1]) + DFS(arr, n - 1, now);
}
 
int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), cmp);
    int num;
    while (scanf("%d", &num) != EOF) {
        printf("%d\n", DFS(arr, n, num));
    }
    return 0;
}