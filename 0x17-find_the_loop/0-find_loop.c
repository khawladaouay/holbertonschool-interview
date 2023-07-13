#include "lists.h"
/**
 * find_listint_loop - finds the loop in a linked list
 * @head: head of the list
 * Return: The address of the node where the loop starts
 * or NULL if there is no loop
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *f, *s;

	if ((!head || !(head->next)) || !(head->next->next))
		return (NULL);
	if (head->next->next == head)
		return (head);
	f = head->next->next;
	s = head;
	while (f && f->next)
	{
		if (f == s)
			break;
		s = s->next;
		fast = f->next->next;
	}
	if (!f || !(f->next))
		return (NULL);
	if (s == f)
	{
		f = f->next;
		while (f != head)
		{
			f = f->next;
			if (f == s)
				head = head->next;
		}
		return (head);
	}
	return (NULL);
}
