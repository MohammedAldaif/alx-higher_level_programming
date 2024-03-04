#include "lists.h"

/**
 * insert_node - function
 * @head: pointer
 * @number: int
 * Return: pointer to struct
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	current = *head;

	new = malloc(sizeof(listint_t));
	temp = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (temp == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > new->n)
			{
				temp = current->next;
				current->next = new;
				new->next = temp;
				break;
			}
			current = current->next;
		}
		current->next = new;
	}
	return (new);
}
