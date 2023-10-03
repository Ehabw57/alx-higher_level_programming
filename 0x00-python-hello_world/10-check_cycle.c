#include "lists.h"
/**
*check_cycle - checks cycles in a linked list
*@list: the list to check
*Return: 0 if cycle is found 1 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *currnt;
	currnt = list;

	while(currnt != NULL)
	{
		currnt = currnt->next;
		if (currnt == list)
		return (1);
	}
	return (0);
}
