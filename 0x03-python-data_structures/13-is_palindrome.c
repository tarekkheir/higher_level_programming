#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if list is palindrome
 * @head: linked list
 * Return: integer 1 if its true or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int tab[512];
	int i = 0;
	int j = 0;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current)
	{
		tab[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	while (tab[i] != tab[j])
	{
		j++;
		i--;
	}

	if (i < j)
		return (0);
	else
		return (1);
}
