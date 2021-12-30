#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 1000
#define Half_Size 500
typedef struct Node node;
struct Node {
    int count;
    char array[SIZE];
    struct Node *next;
};
void printf_list(node *head)
{
    // FILE *f = fopen("test.txt", "w");
    char buff[50000], last = '\0';
    int res_count = 0, len = 0, mxlen = 0;
    while (head) {
        for (int i = 0; i < head->count; i++) {
            if (last != head->array[i]) {
                len = 1;
            }
            else {
                len++;
            }
            if (len > mxlen) {
                mxlen = len;
                res_count = 0;
                buff[res_count] = head->array[i];
                res_count++;
            }
            else if (len == mxlen) {
                buff[res_count] = head->array[i];
                res_count++;
            }
            // printf("%c", head->array[i]);
            last = head->array[i];
        }
        head = head->next;
        // printf(" | ");
    }
    // printf("\n");
    for (int i = 0; i < res_count; i++) {
        printf("%c ", buff[i]);
    }
    printf("%d\n", mxlen);
    // fclose(f);
    return;
}
int main()
{
    char buff[7], pos[6], c[2];
    node *head = (node *)malloc(sizeof(node));
    node *tail = head;
    head->count = 0;
    head->next = NULL;
    int count_of_node = 1;
    while (scanf("%s", buff) != EOF) {
        scanf("%s", pos);
        int status;
        if (strcmp(pos, "left") == 0) {
            status = 1;
        }
        else if (strcmp(pos, "right") == 0) {
            status = 2;
        }
        else {
            status = 3;
        }
        if (strcmp(buff, "insert") == 0) {
            scanf("%s", c);
            if (status == 1) {
                if (head->count + 1 <= SIZE) {
                    // printf("zone 1\n");
                    for (int i = head->count; i > 0; i--) {
                        head->array[i] = head->array[i - 1];
                    }
                    head->array[0] = c[0];
                    head->count++;
                }
                else {
                    // printf("zone 2\n");
                    node *newhead = (node *)malloc(sizeof(node));
                    count_of_node++;
                    newhead->next = head;
                    newhead->array[0] = c[0];
                    for (int i = 0; i < Half_Size; i++) {
                        newhead->array[i + 1] = head->array[i];
                        head->array[i] = head->array[i + Half_Size];
                    }
                    newhead->count = Half_Size + 1;
                    head->count = Half_Size;
                    head = newhead;
                }
            }
            else if (status == 2) {
                if (tail->count + 1 <= SIZE) {
                    // printf("zone 3\n");
                    tail->array[tail->count] = c[0];
                    tail->count++;
                }
                else {
                    // printf("zone 4\n");
                    node *newtail = (node *)malloc(sizeof(node));
                    count_of_node++;
                    tail->next = newtail;
                    newtail->next = NULL;
                    for (int i = 0; i < Half_Size; i++) {
                        newtail->array[i] = tail->array[i + Half_Size];
                    }
                    newtail->array[Half_Size] = c[0];
                    newtail->count = Half_Size + 1;
                    tail->count = Half_Size;
                    tail = newtail;
                }
            }
            else {
                // printf("zone 5\n");
                int num;
                sscanf(pos, "%d", &num);
                node *tmp = head;
                int cnt = 0, rec = 0;
                cnt = tmp->count;
                while (tmp->next && cnt < num) {
                    tmp = tmp->next;
                    cnt += tmp->count;
                    rec++;
                }
                if (rec >= 1) {
                    cnt = 0;
                    node *last = head;
                    for (int i = 0; i < rec; i++) {
                        cnt += last->count;
                        last = last->next;
                    }
                    cnt = num - cnt - 1;
                }
                else {
                    cnt = num - 1;
                }
                if (tmp->count + 1 <= SIZE) {
                    // printf("zone 6 %d %d\n", tmp->count, cnt);
                    for (int i = tmp->count; i > cnt; i--) {
                        tmp->array[i] = tmp->array[i - 1];
                    }
                    tmp->array[cnt] = c[0];
                    tmp->count++;
                }
                else {
                    // printf("zone 7 %d %d\n", tmp->count, cnt);
                    node *newtmp = (node *)malloc(sizeof(node));
                    if (rec == count_of_node - 1) {
                        tail = newtmp;
                    }
                    count_of_node++;
                    node *p = tmp->next;
                    tmp->next = newtmp;
                    newtmp->next = p;
                    if (cnt < Half_Size) {
                        for (int i = 0; i < Half_Size; i++) {
                            newtmp->array[i] = tmp->array[i + Half_Size];
                        }
                        for (int i = Half_Size; i > cnt; i--) {
                            tmp->array[i] = tmp->array[i - 1];
                        }
                        tmp->array[cnt] = c[0];
                        tmp->count = Half_Size + 1;
                        newtmp->count = Half_Size;
                    }
                    else {
                        for (int i = Half_Size; i < cnt; i++) {
                            newtmp->array[i - Half_Size] = tmp->array[i];
                        }
                        newtmp->array[cnt - Half_Size] = c[0];
                        for (int i = cnt; i < SIZE; i++) {
                            newtmp->array[i - Half_Size + 1] = tmp->array[i];
                        }
                        tmp->count = Half_Size;
                        newtmp->count = Half_Size + 1;
                    }
                }
            }
        }
        else {
            if (status == 1) {
                if (head->count > 1) {
                    // printf("zone 8\n");
                    for (int i = 0; i < head->count; i++) {
                        head->array[i] = head->array[i + 1];
                    }
                    head->count--;
                }
                else {
                    // printf("zone 9\n");
                    if (head->next) {
                        node *newhead = head->next;
                        count_of_node--;
                        free(head);
                        head = newhead;
                    }
                    else {
                        head->count--;
                    }
                }
            }
            else if (status == 2) {
                if (tail->count > 1) {
                    // printf("zone 10\n");
                    tail->count--;
                }
                else {
                    if (count_of_node > 2) {
                        // printf("zone 11\n");
                        node *new_tail = head;
                        for (int i = 0; i < count_of_node - 2; i++) {
                            new_tail = new_tail->next;
                        }
                        new_tail->next = NULL;
                        free(tail);
                        count_of_node--;
                        tail = new_tail;
                    }
                    else {
                        tail->count--;
                    }
                }
            }
            else {
                // printf("zone 12\n");
                int num;
                sscanf(pos, "%d", &num);
                node *tmp = head;
 
                int cnt = tmp->count, rec = 0;
                while (tmp->next && cnt < num) {
                    tmp = tmp->next;
                    cnt += tmp->count;
                    rec++;
                }
                if (rec >= 1) {
                    cnt = 0;
                    node *last = head;
                    for (int i = 0; i < rec; i++) {
                        cnt += last->count;
                        last = last->next;
                    }
                    cnt = num - cnt - 1;
                }
                else {
                    cnt = num - 1;
                }
 
                if (tmp->count > 1) {
                    // printf("zone 13 %d,%d\n", tmp->count, cnt);
                    for (int i = cnt; i < tmp->count - 1; i++) {
                        tmp->array[i] = tmp->array[i + 1];
                    }
                    tmp->count--;
                }
                else if (count_of_node <= 1) {
                    tmp->count--;
                }
                else {
                    // printf("zone 14\n");
                    node *last = head;
                    if (rec >= 2) {
                        for (int i = 0; i < rec - 1; i++) {
                            last = last->next;
                        }
                        last->next = tmp->next;
                    }
                    else {
                        head = tmp->next;
                    }
                    if (rec == count_of_node - 1) {
                        tail = last;
                    }
                    free(tmp);
                    count_of_node--;
                }
            }
        }
        // printf("%d %d\n", head->count, tail->count);
        // printf_list(head);
    }
    printf_list(head);
    // system("pause");
    return 0;
}