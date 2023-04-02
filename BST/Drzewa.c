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

int height(struct tree *root) {
    if (root == NULL) {
        return -1; // height of an empty tree is -1
    } else {
        int left_height = height(root->left);
        int right_height = height(root->right);
        return 1 + (left_height > right_height ? left_height : right_height);
    }
}

int count_nodes(struct tree* node) {
    if (node == NULL)
        return 0;
    return 1 + count_nodes(node->left) + count_nodes(node->right);
}

struct tree* sorted_array_to_avl(int arr[], int start, int end) {
    if (start > end)
        return NULL;

    int mid = (start + end) / 2;
    struct tree* root = (struct tree*)malloc(sizeof(struct tree));
    root->info = arr[mid];
    root->left = sorted_array_to_avl(arr, start, mid - 1);
    root->right = sorted_array_to_avl(arr, mid + 1, end);
    return root;
}

void inorder_to_array(struct tree* node, int arr[], int* i) {
    if (node == NULL){
        return;
    }
    inorder_to_array(node->left, arr, i);
    arr[(*i)++] = node->info;
    inorder_to_array(node->right, arr, i);
}

struct tree* bst_to_avl(struct tree* root) {
    int n = count_nodes(root);
    int* arr = (int*)malloc(n * sizeof(int));
    int i = 0;
    inorder_to_array(root, arr, &i);
    struct tree* new_root = sorted_array_to_avl(arr, 0, n - 1);
    free(arr);
    return new_root;
}

int main(){
    struct tree *root = NULL; // initialize root to NULL
	
    root = insert(root, 5); // add value 5 to the binary search tree
	root = insert(root, 10); // add value 10 to the binary search tree
	root = insert(root, 3); // add value 3 to the binary search tree
	root = insert(root, 11); // add value 10 to the binary search tree
	root = insert(root, 12); // add value 3 to the binary search tree
	root = insert(root, 13); // add value 10 to the binary search tree
	root = insert(root, 14); // add value 3 to the binary search tree
	root = insert(root, 15); // add value 10 to the binary search tree
	root = insert(root, 16); // add value 3 to the binary search tree
	
    inorder(root);
	printf("\n");


	printf("%d\n",height(root));

	root = bst_to_avl(root);
	printf("%d\n",height(root));

    
    return 0;
}