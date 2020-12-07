#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 *check_cycle - check if the there is a cycle in the linked list
 *@head: list
 *Return: 1 if there is a cycle and 0 if not
 */
int check_cycle(listint_t *head)
{
	listint_t *one_step = NULL;
	listint_t *two_step = NULL;

	if (head == NULL)
		return (0);

	two_step = head;
	one_step = two_step->next;
	two_step = one_step->next;

	while (head && one_step && two_step)
	{
		if (head == one_step || head == two_step)
			return (1);

		head = head->next;
		one_step = two_step->next;
		two_step = one_step->next;
	}

	return (0);
}
