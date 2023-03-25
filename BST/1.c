#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node * next;
} node_t;

void print_list(node_t * head) {
    node_t * current = head;

    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }
    printf("\n");
}

void push(node_t * head, int A) {
    node_t * current = head;    
    while ((current->next != NULL)&&((current->next->val)<A)) { 
        current = current->next;
    }
    node_t * temp2 = NULL;
    temp2 = (node_t *) malloc(sizeof(node_t));
    temp2->val=A;
    temp2->next=current->next;

    current->next=temp2;
}


int main(){

node_t * test_list = NULL;
test_list = (node_t *) malloc(sizeof(node_t));
test_list->val = 1;
test_list->next = (node_t *) malloc(sizeof(node_t));
test_list->next->val = 3;
test_list->next->next = NULL;

print_list(test_list);

push(test_list,4);
print_list(test_list);

push(test_list,2);
print_list(test_list);
    return 0;
}
