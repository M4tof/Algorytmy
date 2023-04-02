#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    FILE* file = fopen("Wyniki2.txt", "w");
    
    struct tree *root = NULL; // initialize root to NULL


    fclose(file);
    return 0;
}