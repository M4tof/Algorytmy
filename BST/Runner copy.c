#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

#define MAX_LINE_LENGTH 1000
#define MAX_NUMBERS_PER_LINE 100

void submain(int LArray,int AArray[]){
    printf("-----------\n");

    node * lista = NULL;
    lista = (node *) malloc(sizeof(node));

    for(int i=0; i<LArray; i++){
        Add(lista,&lista,AArray[i]);
    }

    print_list(lista);
    printf("_\n");

    for(int i=0;i<LArray;++i){
        printf("%d\n",Serch(lista,AArray[i]));
    }

    DeleteList(&lista);

    printf("_\n");
    struct tree *root = NULL; // initialize root to NULL
            
    for(int i=0; i<LArray; i++){
        root = insert(root, AArray[i]);
    }

    for(int i=0;i<LArray;++i){
            search(root,AArray[i]);
    }

    inorder(root);

    
    DeleteTree(root);

    printf("\n-----------\n");
}



int main() {
    FILE* file = fopen("Liczby.txt", "r");
    if (!file) {
        printf("Failed to open file\n");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    int numbers[MAX_NUMBERS_PER_LINE];
    int num_numbers;

    while (fgets(line, MAX_LINE_LENGTH, file)) {
        num_numbers = 0;


        char* token = strtok(line, " \n");
        while (token) {
            numbers[num_numbers++] = atoi(token);
            token = strtok(NULL, " \n");
        }
        
        for (int i = 0; i < num_numbers; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");

        // TODO: Process the array as needed
        submain(num_numbers,numbers);
    }

    fclose(file);
    return 0;
}