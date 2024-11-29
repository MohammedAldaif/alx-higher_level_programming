#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int n) {
    listint_t *new;       /* New node to insert */
    listint_t *current;   /* Pointer to traverse the list */

    /* Allocate memory for the new node */
    new = malloc(sizeof(listint_t));
    if (new == NULL) {
        return (NULL); /* Memory allocation failure */
    }

    new->n = n;

    /* Case 1: Insert at the beginning or into an empty list */
    if (*head == NULL || (*head)->n >= n) {
        new->next = *head;
        *head = new;
        return (new);
    }

    /* Case 2: Traverse to find the correct position */
    current = *head;
    while (current->next != NULL && current->next->n < n) {
        current = current->next;
    }

    /* Insert the new node in the correct position */
    new->next = current->next;
    current->next = new;

    return (new);
}
