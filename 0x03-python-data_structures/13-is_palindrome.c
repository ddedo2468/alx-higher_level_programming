#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome_recursive - recursively checks if a list is a palindrome
 * @left: left pointer
 * @right: right pointer
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome_recursive(listint_t **left, listint_t *right)
{
    if (right == NULL)
        return (1);

    int is_palindrome = is_palindrome_recursive(left, right->next);

    if (!is_palindrome)
        return (0);

    is_palindrome = ((*left)->n == right->n);

    *left = (*left)->next;

    return (is_palindrome);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1);

    return (is_palindrome_recursive(head, *head));
}
