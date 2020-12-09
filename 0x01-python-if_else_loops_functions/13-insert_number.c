#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *current = NULL;
	listint_t *prec = NULL;
	int tmp = 0;

	if (*head == NULL)
	{
		add_nodeint_end(head, number);
		return (*head);
	}
	current = *head;
	prec = *head;
	node = malloc(sizeof(listint_t));
	node->n = number;
	tmp = current->n;

	if (tmp >= number)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	current = current->next;

	if (current)
	{
		while (current)
		{
			if (tmp <= number && current->n > number)
			{
				prec->next = node;
				node->next = current;
				return (node);
			}
			if (current->next == NULL && current->n < number)
			{
				add_nodeint_end(head, number);
				return (node);
			}
			tmp = current->n;
			prec = current;
			current = current->next;
		}
	}
	else
		current->next = node;
	node->next = NULL;
	return (node);
}
