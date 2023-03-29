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

void add(node_t ** head, int A) {
    
    node_t * new_node = NULL;
    new_node = (node_t *) malloc(sizeof(node_t));
    new_node->val = A;
    new_node->next = *head;
    *head = new_node;
}

void new(node_t * head, int A){
    node_t * current = head;
    current->val = A;
    current->next = NULL;
}

int lowest(node_t * head){
    node_t * current = head;
    return (current->val);
}

int main(){

node_t * test_list = NULL;
test_list = (node_t *) malloc(sizeof(node_t)); //Create and Name

new(test_list,2); //First data
print_list(test_list);

push(test_list,5); //add behind first
print_list(test_list);

push(test_list,3);
print_list(test_list);

add(&test_list,1); //add at first
print_list(test_list);

printf("%d",lowest(test_list));// current lowest number

    return 0;
}
