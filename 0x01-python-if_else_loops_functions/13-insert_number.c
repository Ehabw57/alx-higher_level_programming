#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currnt = *head, *forward = NULL;

		forward = malloc(sizeof(listint_t));
		if (forward == NULL)
				return (NULL);
		forward->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		forward->next = *head;
		*head = forward;
		return (*head);
	}

	while ( currnt->next != NULL && currnt->next->n < number)
		currnt = currnt->next;

	forward->next = currnt->next;
	currnt->next = forward;
	return (*head);
}
