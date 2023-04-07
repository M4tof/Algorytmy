#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    FILE* file = fopen("Wyniki2.txt", "w");
    
    struct tree *root = NULL; // initialize root to NULL

    for(int Big=1;Big<=30;Big++){
        double NBig = 1000*Big;
        int* array = generate_random_array(NBig); //List of randome numbers
        
        /////////////////Tree Creation///////////////////////
        fprintf(file,"BST:");
        fprintf(file,"%d",Big);
        fprintf(file,":");
        printf("Starting runner for Tree creation %d:\n",Big);

        struct tree *root = NULL; // initialize root to NULL
            
        for(int i=1; i<=NBig; i++){
            root = insert(root, array[i]);
        }

        int BSTh = height(root);
        fprintf(file,"%d\n",BSTh);

        root = bst_to_avl(root);
        fprintf(file,"AVL:%d:%d\n",Big,height(root));


        DeleteTree(root);
        /////////////////////////////////////////////////////////////
        }
    fclose(file);
    return 0;

}