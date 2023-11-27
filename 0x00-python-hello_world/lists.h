#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_s;

size_t print_listint(const listint_s *h);
listint_s *add_nodeint(listint_s **head, const int n);
void free_listint(listint_s *head);
int check_cycle(listint_s *list);

#endif /* LISTS_H */
