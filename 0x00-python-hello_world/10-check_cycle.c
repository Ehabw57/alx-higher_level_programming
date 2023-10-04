#include "lists.h"
/**
*check_cycle - checks cycles in a linked list
*@list: the list to check
*Return: 0 if cycle is found 1 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *tor = NULL, *hare = NULL, *tmp = NULL;
	tor = list;
	tmp = list->next;
	hare = tmp->next;

	while(tmp->next != NULL)
	{
		tmp = hare->next;
		hare = tmp->next;
		tor = tor->next;
		if (hare == tor)
		return (1);
	}
	return (0);
}
