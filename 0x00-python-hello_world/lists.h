#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list_node - Singly linked list node
 * @n: Integer value
 * @next: Pointer to the next node
 *
 * Description: A structure representing a node in a singly linked list.
 */
typedef struct list_node
{
        int n;
        struct list_node *next;
} list_node;


#endif
