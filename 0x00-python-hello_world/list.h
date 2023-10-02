#ifndef LIST_H
#define LIST_H

/* Define a structure for a singly linked list node */
typedef struct ListNode {
    int data;       
    struct ListNode* next; 
} ListNode;

/* Function prototypes */
ListNode* createNode(int data);
void insertNode(ListNode** head, int data);
void deleteNode(ListNode** head, int data);
void printList(ListNode* head);
void freeList(ListNode* head);



#endif
