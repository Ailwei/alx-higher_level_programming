#include "lists.h"

int is_palindrome(listint_t **head)
{
	int length = strlen(head);
	int i;
	for (i = 0; i < length / 2; i++)
	{
		if (head[i] != head[length - i -1])
		{
			return false;
		}
	}
	return true;
}
