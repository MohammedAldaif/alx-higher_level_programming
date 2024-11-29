#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int n) {
    listint_t *new;
    listint_t *current;
    listint_t *step = NULL;

    current = *head;

    /* Allocate memory for the new node */
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    /* Traverse the list to find the correct position */
    while (current->next != NULL && current->next->n < n) {
        current = current->next;
        step = current->next;
    }

    /* Insert the new node */
    current->next = new;
    new->next = step;

    return (new);
}
