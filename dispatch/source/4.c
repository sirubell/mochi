#include<stdio.h>
int main()
{
    int as[1000000];
    for(int i=0;i<1000000;i++)as[i]=9;
    int first=0;
    int people,number;
    scanf("%d%d",&people,&number);
    int numbers[people][number][number];
    char name[people][20];
    int now[people][number*number];
    for(int i=0;i<people;i++)
    {
        scanf("%s",name[i]);
        for(int v1=0;v1<number;v1++)
        {
            for(int v2=0;v2<number;v2++)
            {
                scanf("%d",&numbers[i][v1][v2]);
            }
        }
    }
    for(int i=0;i<people;i++)
    {
        for(int v1=0;v1<number;v1++)
        {
            for(int v2=0;v2<number;v2++)
            {
                int temp=numbers[i][v1][v2];
                now[i][temp]=v1*number+v2;
            }
        }
    }
    int now_number;
    while(scanf("%d",&now_number)!=EOF)
    {
        for(int i=0;i<people;i++)
        {
            int temp=now[i][now_number];
            int x=temp/number;
            int y=temp%number;
            numbers[i][x][y]=-1;
        }
        for(int i=0;i<people;i++)
        {
            int jump=0;
            if(jump==0)
            {
                {
                    int count=0;
                    for(int v1=0;v1<number;v1++)
                    {
                        if(numbers[i][v1][v1]==-1)
                        {
                        }else
                        {
                            count=1;
                            break;
                        }
                    }
                    if(count==0)
                    {
                        if(first==0)
                        {
                            printf("%d %s",now_number,name[i]);
                            first=1;
                            jump=1;
                        }else
                        {
                            printf(" %s",name[i]);
                            jump=1;
                        }
                    }
                }
            }else
            {
                continue;
            }
            if(jump==0)
            {
                {
                    int count=0;
                    for(int v1=0;v1<number;v1++)
                    {
                        if(numbers[i][v1][number-v1-1]==-1)
                        {
                        }else
                        {
                            count=1;
                            break;
                        }
                    }
                    if(count==0)
                    {
                        if(first==0)
                        {
                            printf("%d %s",now_number,name[i]);
                            first=1;
                            jump=1;
                        }else
                        {
                            printf(" %s",name[i]);
                            jump=1;
                        }
                    }
                }
            }else
            {
                continue;
            }
            if(jump==0)
            {
                for(int v1=0;v1<number;v1++)
                {
                    int count=0;
                    for(int v2=0;v2<number;v2++)
                    {
                        if(numbers[i][v1][v2]==-1)
                        {
                        }else
                        {
                            count=1;
                            break;
                        }
                    }
                    if(count==0)
                    {
                        if(first==0)
                        {
                            printf("%d %s",now_number,name[i]);
                            first=1;
                            jump=1;
                        }else
                        {
                            printf(" %s",name[i]);
                            jump=1;
                        }
                    }
                }
            }else
            {
                continue;
            }
            if(jump==0)
            {
                for(int v1=0;v1<number;v1++)
                {
                    int count=0;
                    for(int v2=0;v2<number;v2++)
                    {
                        if(numbers[i][v2][v1]==-1)
                        {
                        }else
                        {
                            count=1;
                            break;
                        }
                    }
                    if(count==0)
                    {
                        if(first==0)
                        {
                            printf("%d %s",now_number,name[i]);
                            first=1;
                            jump=1;
                        }else
                        {
                            printf(" %s",name[i]);
                            jump=1;
                        }
                    }
                }
            }else
            {
                continue;
            }
        }
        if(first!=0)
        {
            break;
        }
    }
}