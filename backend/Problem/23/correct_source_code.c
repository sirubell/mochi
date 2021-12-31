#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n,m;
    char player[10][64];
    scanf("%d%d",&n,&m);
    int player_bingo[n][m][m],player_end[n],numbertoindex[n][m*m],index[n][m*m];
    for(int i=0;i<n;i++)
    {   
        player_end[i]=0;
        scanf("%s",player[i]);
        for(int bi=0;bi<m;bi++)
            for(int bj=0;bj<m;bj++)
            {
                    scanf("%d",&player_bingo[i][bi][bj]);
                    //printf("%d",player_bingo[i][bi][bj]);
            }
    }
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<m;j++)
            {   
                numbertoindex[k][player_bingo[k][i][j]]=i*m+j;
                index[k][i*m+j]=1;
            }
        }
    }
    int input,end1=0,end2=0,end3=0,end4=0,endend=0,temp,i1,j1;
    for(int in=0;in<m*m;in++)
    {
        scanf("%d",&input);
        for(int playerrr=0;playerrr<n;playerrr++)
        {   
            index[playerrr][numbertoindex[playerrr][input]]=0;
            //printf("%d\n",numbertoindex[playerrr][input]);
            //if(in>=m-1)
            i1=numbertoindex[playerrr][input]/m;
            j1=numbertoindex[playerrr][input]%m;
 
            if((i1-j1)==0)
            {   
                for(int i=0;i<m;i++)
                {
                    if(index[playerrr][i*m+i]==0)
                        end3++; 
                }
                if(end3==m)
                {
                    player_end[playerrr]=1;
                    //printf("%d use 3 to pass\n",playerrr);
                }
            }
            if((i1+j1)==m-1)
            {
                for(int i=0;i<m;i++)
                {   
                    if(index[playerrr][(i+1)*m-1-i]==0)
                    end4++;
                }
                if(end4==m)
                {
                    player_end[playerrr]=1;
                    //printf("%d use four to pass\n",playerrr);
                }
            }
            end3=0;
            end4=0;
            if (player_end[playerrr]!=1)
            {
                end1=0;    
                for(int i=0;i<m;i++)
                {
                    if(index[playerrr][i1*m+i]==0)
                        end1++;
                }
 
                if(end1==m)
                {  
                    player_end[playerrr]=1;
                    //printf("%d use 1 to pass\n",playerrr);
                    //printf("%d,%d,%d",i1,j1,input);
                }
                end2=0;
                for(int i=0;i<m;i++)
                {    
                    if(index[playerrr][i*m+j1]==0)
                        end2++;
                } 
                if(end2==m)
                {
                    player_end[playerrr]=1;
                    //printf("%d use 2 to pass\n",playerrr);
                }
 
            }            
            if (player_end[playerrr]==1)  
                endend=1;       
        }
        //printf("%d,%d",i1,j1);
        if(endend==1)
        {
            printf("%d",input);        
            break;
        }
    }
 
    for(int i =0;i<n;i++)
    {
        if (player_end[i]==1)
        {
            printf(" %s",player[i]);
            endend=1;
        }        
    }
    // system("pause");
    return 0;
}