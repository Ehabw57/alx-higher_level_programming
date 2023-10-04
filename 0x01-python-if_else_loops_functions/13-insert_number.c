#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currnt = *head, *forward = *head;

	if (*head == NULL || forward->n > number)
	{
		forward = malloc(sizeof(listint_t));
		if (forward == NULL)
				return (NULL);
		forward->n = number;
		forward->next = *head;
		*head = forward;
		return (*head);
	}

	while (currnt != NULL)
	{
		forward = forward->next;
		if (forward == NULL || forward->n > number)
		{
			forward = malloc(sizeof(listint_t));
			if (forward == NULL)
				return (NULL);
			forward->n = number;
			forward->next = currnt->next;
			currnt->next = forward;
			return (*head);
		}
		currnt = currnt->next;
	}

	return (NULL);
}
