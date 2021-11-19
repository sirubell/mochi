#include<stdio.h>
int main()
{
    int number;
    scanf("%d",&number);
    int numbers[number];
    for(int i=0;i<number;i++)
    {
        scanf("%d",&numbers[i]);
    }
    int check=0;
    for(int i=0;i<number;i++)
    {
        if(numbers[i]%2==1)
        {
            if(check==0)
            {
                printf("%d",numbers[i]);
                check++;
            }else {
                printf(" %d",numbers[i]);
            }
        }
    }
    printf("\n");
    check=0;
    for(int i=0;i<number;i++)
    {
        if(numbers[i]%2==0)
        {
            if(check==0)
            {
                printf("%d",numbers[i]);
                check++;
            }else {
                printf(" %d",numbers[i]);
            }
        }
    }
}