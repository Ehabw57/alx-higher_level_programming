#include "lists.h"

/**
 * check_cycle - checks cycles in a linked list
 * @list: the list to check
 * Return: 0 if cycle is found, 1 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
