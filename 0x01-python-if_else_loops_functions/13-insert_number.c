#include "lists.h"
#include <stdio.h>

/**
  * insert_node - function to insert a new node in a sort linked list
  * @head: the head node of the linked list
  * @number: content of the node to insert
  * Return: the address of the new node
  **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new_node;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	while (current_node->next)
	{
		if (current_node->next->n > number)
			break;
		current_node = current_node->next;
	}
	if (!current_node->next)
	{
		new_node->next = current_node->next;
		new_node->n = number;
		current_node->next = new_node;
	}
	else if (current_node->next->n > number)
	{
		new_node->next = current_node->next;
		new_node->n = number;
		current_node->next = new_node;
	}
	return (new_node);
}
