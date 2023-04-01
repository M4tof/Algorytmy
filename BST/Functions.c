#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

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

void newlist(node * head, int A){ // node * listname =NULL; listname = (node *) malloc(sizeof(node)); newlist(listname,value);
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
        newlist(head,A);
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

////////////////////////////////////////BST///////////////////////////////////////////////////

struct tree {
	int info;
	struct tree *left;
	struct tree *right;
};

struct tree *insert(struct tree *root, int x){
	if(!root) {
		root=(struct tree*)malloc(sizeof(struct tree));
		root->info = x;
		root->left = NULL;
		root->right = NULL;
		return(root);
	}
	if(root->info > x)
	     root->left = insert(root->left,x); else {
		if(root->info < x)
			root->right = insert(root->right,x);
	}
	return(root);
}

struct tree *search(struct tree *root, int x){
    struct tree *ptr;
    ptr = root;
    while(ptr) {
        if(x > ptr->info)
            ptr = ptr->right; 
        else if(x < ptr->info)
            ptr = ptr->left; 
        else
            return ptr; // return the pointer to the found node
    }
    return NULL; // return NULL if the node is not found
}

void inorder(struct tree *root){
	if(root != NULL) {
		inorder(root->left);
		printf(" %d",root->info);
		inorder(root->right);
	}
	return;
}

void postorder(struct tree *root){
	if(root != NULL) {
		postorder(root->left);
		postorder(root->right);
		printf(" %d",root->info);
	}
	return;
}

void preorder(struct tree *root){
	if(root != NULL) {
		printf(" %d",root->info);
		preorder(root->left);
		preorder(root->right);
	}
	return;
}

void DeleteTree(struct tree *root){
    if (root != NULL){
        DeleteTree(root->left);
        DeleteTree(root->right);
        free(root);
    }

}
///////////////////////////////////////////////////////////////
int* generate_random_array(int length) {
    int* array = malloc(length * sizeof(int));

    // initialize the array with unique random integers
    srand(time(NULL));
    for (int i = 0; i < length; i++) {
        int rand_int;
        do {
            rand_int = rand();
            // check if rand_int already exists in the array
            int exists = 0;
            for (int j = 0; j < i; j++) {
                if (array[j] == rand_int) {
                    exists = 1;
                    break;
                }
            }
            if (!exists) {
                array[i] = rand_int;
                break;
            }
        } while (1);
    }

    return array;
}