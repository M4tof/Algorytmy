#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>    

typedef struct Node {
    int key;
    struct Node *next;
}node;

bool Empty = true;

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

void DeleteList(node **head) { //DeleteList(&listname);
    node *current = *head;
    
    while (current != NULL) {
        *head = current->next;
        free(current);
        current = *head;
    }
    *head = NULL;
    Empty=true;
}

int Lowest(node * head){ //Lowest(listname);
    node * current = head;
    return (current->key);
}

void Add(node *head,node **head2,int A){ //Add(listname,&listname,value);
    if (Empty==true){
        new(head,A);
        Empty=false;
    }
    else{
        if (A < Lowest(head)){
        InsertHead(head2,A);
        }
        if (A > Lowest(head)){
        InsertNext(head,A);
        }
        else{
        
        }
    }
}


int main(){
    node * test_list = NULL;
    test_list = (node *) malloc(sizeof(node)); //Create and Name
    
    Add(test_list,&test_list,1);
    Add(test_list,&test_list,3);
    Add(test_list,&test_list,5);
    Add(test_list,&test_list,7);
    Add(test_list,&test_list,9);
    Add(test_list,&test_list,2);
    Add(test_list,&test_list,4);
    Add(test_list,&test_list,6);
    Add(test_list,&test_list,0);
    Add(test_list,&test_list,8);
    print_list(test_list);
    

    DeleteHead(&test_list);
    DeleteLast(test_list);
    DeleteSpecific(&test_list,1);
    print_list(test_list);
    DeleteList(&test_list);
        
    return 0;

}
