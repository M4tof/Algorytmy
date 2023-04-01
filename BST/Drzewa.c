#include <stdio.h>
#include <stdlib.h>

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

int main(){
    struct tree *root = NULL; // initialize root to NULL
	
    root = insert(root, 5); // add value 5 to the binary search tree
	root = insert(root, 10); // add value 10 to the binary search tree
	root = insert(root, 3); // add value 3 to the binary search tree
	
    inorder(root);
    printf("pre\n");
    DeleteTree(root);
    printf("done\n");
    inorder(root);
    printf("END\n");
    
    return 0;
}