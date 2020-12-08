#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *current = NULL;
	listint_t *prec = NULL;
	int tmp = 0;

	current = *head;
	prec = *head;
	node = malloc(sizeof(listint_t));
	node->n = number;
	tmp = current->n;

	if (tmp >= number)
	{
		node->next = current;
		return (node);
	}
	current = current->next;

	if (current)
	{
		while (current->next)
		{
			if (tmp <= number && current->n >= number)
			{
				prec->next = node;
				node->next = current;
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
