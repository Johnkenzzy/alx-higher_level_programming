#include "lists.h"


/**
 * check_cycle - Checks if a singly linked list has a cycle/loop in it
 * @list: singly linked list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *move_slow = list, *move_fast = list;

	while (move_slow != NULL && move_fast != NULL && move_fast->next != NULL)
	{
		move_slow = move_slow->next;
		move_fast = move_fast->next->next;

		if (move_slow == move_fast)
			return (1);
	}
	return (0);
}
