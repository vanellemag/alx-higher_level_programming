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
	int i = 0, j, l;
	listint_t *front, *rear;

	l = len(head);
	while (i != l / 2)
	{
		front = rear = *head;
		for (j = 0; j < i; j++)
		{
			front = front->next;
		}
		for (j = 0; j < l - (i + 1); j++)
		{
			rear = rear->next;
		}
		if (front->n != rear->n)
		{
			return (0);
		}
		else
		{
			i++;
		}
	}
	return (1);
}
