#include "lists.h"
/**
 * is_palindrome - checks whether a linked list is palindorme or not
 * @head: pointer to the head of the list
 * Return: 1 if list is palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *move = NULL;
	int *nums = NULL;
	int lenth = 0, i = 0;

	/*clac the lenth of the list*/
	for (move = (*head); move != NULL; lenth++)
		move = move->next;

	/*checks if list is only 1 node or less*/
	if (lenth <= 1 || *head == NULL)
		return (1);

	i = lenth / 2;
	nums = malloc(sizeof(int) * i);

	/*move ptr to the half of the list while copying it reversly*/
	for (move = (*head); i > 0; i--)
	{
		nums[i - 1] = move->n;
		move = move->next;
	}

	/*compare both list and nums*/
	for (i = 0; nums[i] == move->n; i++)
	{
		if (i >= (lenth / 2) - 1)
		{
			free(nums);
			return (1);
		}
		move = move->next;
	}
	free(nums);
	return (0);
}
