#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;        /* Move one step */
		fast = fast->next->next;  /* Move two steps */

		if (slow == fast)
			return (1); /* If they meet, there is a cycle */
	}

	return (0); /* If fast reaches the end, there is no cycle */
}
