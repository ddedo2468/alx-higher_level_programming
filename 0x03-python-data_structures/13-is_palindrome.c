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
    int is_palindrome = 1; // Assume it's a palindrome by default

    if (*head == NULL || (*head)->next == NULL)
        return (1); // Empty list or single element is a palindrome

    // Find the middle of the list using slow and fast pointers
    while (fast && fast->next)
    {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
    }

    // If the list has an odd number of elements, ignore the middle element
    if (fast)
    {
        second_half = slow->next;
        slow->next = NULL;
    }
    else
    {
        second_half = slow;
    }

    // Reverse the second half of the list
    while (second_half)
    {
        temp = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = temp;
    }

    second_half = prev; // New head of the reversed second half

    // Compare the first half and reversed second half
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

