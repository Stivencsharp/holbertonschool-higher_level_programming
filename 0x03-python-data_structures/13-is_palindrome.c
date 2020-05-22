#include "lists.h"

/**
  * is_palindrome - Function to check if a linked list is a palindrome
  * @head: the first node of the list
  * Return: 1 if it is not a palindrome and 0 if it is a palindrome
  **/

int is_palindrome(listint_t **head)
{
	listint_t *second_part = *head;
	listint_t *first_part = *head;

	if (!first_part->next)
		return (1);
	return (pal(&first_part, second_part));
}

/**
   * pal - Function to check the palindrome
   * @fn: first part node
   * @sn: second part node
   * Return: 1 or 0 if the list is palindrome
   **/

int pal(listint_t **fn, listint_t *sn)
{
	int n = 1;

	if (sn->next)
		n = pal(fn, sn->next);
	if (n == 0)
		return (1);
	if ((*fn)->n == sn->n)
	{
		(*fn) = (*fn)->next;
		return (1);
	}
	return (0);
}
