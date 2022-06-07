#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked is a palindrome
 * @head: linked list
 * Return: 1 success or 0 failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL, *tmp = NULL;

	start = *head;
	while (start != tmp && start != end)
	{
		tmp = end;
		end = start;
		while (end->next != tmp)
		{
			end = end->next;
		}
		if (start->n != end->n)
			return (0);
		start = start->next;
	}
	return (1);
}
