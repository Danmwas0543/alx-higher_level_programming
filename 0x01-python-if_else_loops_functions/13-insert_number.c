#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - putting a number to a sorted list
 * @number: number being used
 * @head: the linked list
 * Return: pointer to the head which has been created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *recently = *head;
	listint_t *fresh = NULL;
	listint_t *tp = NULL;

	if (!head)
		return (NULL);

	fresh = malloc(sizeof(listint_t));
	if (!fresh)
		return (NULL);
	fresh->n = number;
	fresh->next = NULL;
	if (!*head || (*head)->n > number)
	{
		fresh->next = *head;
		return (*head = fresh);
	}
	else
	{
		while (recently && recently->n < number)
		{
			tp = recently;
			recently = recently->next;
		}
		tp->next = fresh;
		fresh->next = recently;
	}
	return (fresh);
}
