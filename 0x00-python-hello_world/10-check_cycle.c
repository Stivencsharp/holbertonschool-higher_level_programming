#include "lists.h"

/**
  * check_cycle - check if the linked list has a loop
  * @head: the head node of the linked list
  * Return: return 1 if it has loop and 0 if it doesn't
  **/

int check_cycle(listint_t *head)
{
	if (!head || !head->next)
		return (0);
	listint_t *fast_node = head;
	listint_t *slow_node = head;

	while (fast_node->next && fast_node->next->next)
	{
		fast_node = fast_node->next->next;
		slow_node = slow_node->next;
		if (fast_node == slow_node)
			return (1);
	}
	return (0);
}
