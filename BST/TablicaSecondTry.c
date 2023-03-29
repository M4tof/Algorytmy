#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node *next;
}node;

void InsertHead(node ** head, int A){ // InsertHead(&listname,value)
    node * new_node = NULL;
    new_node = (node *) malloc(sizeof(node));
    new_node->key = A;
    new_node->next = *head;
    *head = new_node;
}

void InsertNext(node *head,int A){ // InsertNext(listname,value)
    node * current = head;    
    while ((current->next != NULL)&&((current->next->key)<A)) { 
        current = current->next;
    }
    node * temp2 = NULL;
    temp2 = (node *) malloc(sizeof(node));
    temp2->key=A;
    temp2->next=current->next;
    current->next=temp2;
}

void print_list(node * head) { // print_list(listname)
    node * current = head;
    while (current != NULL) {
        printf("%d\n", current->key);
        current = current->next;
    }
    printf("\n");
}

void new(node * head, int A){ // node * listname =NULL; listname = (node *) malloc(sizeof(node)); new(listname,value);
    node * current = head;
    current->key = A;
    current->next = NULL;
}

void DeleteHead(node **head){ //   DeleteHead(listname);
    node *next_node = NULL;
    next_node = (*head)->next;
    free(*head);
    *head = next_node;
}

void DeleteLast(node *head){ //DeleteLast(listname);
    if(head->next ==NULL){
        free(head);
    }
    node * current = head;
    while (current->next->next != NULL){
        current=current->next;
    }

    free(current->next);
    current->next = NULL;

}

void DeleteSpecific(node **head, int index) { // DeleteSpecific(&listname, index)
    if (*head == NULL) {
        return;
    }
    
    node *prev = NULL;
    node *current = *head;
    int i = 0;
    
    while (current != NULL && i < index) {
        prev = current;
        current = current->next;
        i++;
    }
    
    if (current == NULL) {
        return;
    }
    
    if (prev == NULL) {
        *head = current->next;
    } else {
        prev->next = current->next;
    }
    
    free(current);
}

void DeleteList(node **head) {
    node *current = *head;
    
    while (current != NULL) {
        *head = current->next;
        free(current);
        current = *head;
    }
    *head = NULL;
}

int main(){
    node * test_list = NULL;
    test_list = (node *) malloc(sizeof(node)); //Create and Name

    new(test_list,2);
    InsertHead(&test_list,1);
    InsertNext(test_list,3);
    print_list(test_list);
    DeleteSpecific(&test_list,2);
    print_list(test_list);
    DeleteList(&test_list);
    print_list(test_list);
        return 0;

}
