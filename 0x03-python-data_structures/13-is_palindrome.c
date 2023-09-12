#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp, *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
	return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
	}
	if (fast)
	{
		second_half = slow->next;
		slow->next = NULL;
	}
	else
	second_half = slow;
	while (second_half)
	{
		temp = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = temp;
	}
	second_half = prev;

	while (second_half)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (is_palindrome);
}
