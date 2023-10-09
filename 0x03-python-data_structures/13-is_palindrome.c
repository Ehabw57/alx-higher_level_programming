#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head)
{
    listint_t *move = *head, *new;
    int *nums = NULL;
    int lenth = 0, min = 0;

    /*clac the lenth of the list*/
    while (move != NULL)
    {
        move = move->next;
        lenth++;
    }
    /*checks if list is only 1 node*/
    if (lenth <= 1 || ((*head)->n == (*head)->next->n && lenth == 2))
        return 1;
    /*move ptr to the half of the list*/
    for (move = (*head); min <= lenth / 2; min++)
        move = move->next;

    nums = malloc(sizeof(int) * (min + 1));
    new = move;
    /*store half of the list*/
    while (min >= 0 && move != NULL)
    {
        nums[min] = move->n;
        move = move->next;
        min--;
    }
    move = new;
    /*loop on the list*/
    for (min = 0; nums[min] == move->n; min++)
    {

        if (min >= lenth / 2)
        {
            free(nums);
            return (1);
        }
        move = move->next;
    }
    free(nums);
    return (0);
}
