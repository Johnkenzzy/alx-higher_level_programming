#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * reverse_list - Reverse a singly linked list
 * @head: pointer to pointer to the first node of listint_t list
 *
 * Return: pointer to rversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}


/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to pointer to the first node of listint_t list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int palindrome = 1;
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	listint_t *second_half = NULL, *middle = NULL;
	listint_t *first_half = *head, *second_half_copy = second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			palindrome = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	second_half_copy = reverse_list(second_half_copy);
	if (middle != NULL)
	{
		prev_slow->next = middle;
		middle->next = second_half_copy;
	}
	else
		prev_slow->next = second_half_copy;
	return (palindrome);
}
