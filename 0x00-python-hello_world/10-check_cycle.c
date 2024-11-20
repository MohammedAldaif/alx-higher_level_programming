#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * 
 * Return: 0 if no cycle, 1 if cycle is present
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (list == NULL) /* Empty list has no cycle */
        return 0;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;       /* Move slow by one step */
        fast = fast->next->next; /* Move fast by two steps */

        if (slow == fast) /* Cycle detected */
            return 1;
    }

    return 0; /* No cycle */
}
