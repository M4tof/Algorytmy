#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    FILE* file = fopen("Wyniki2.txt", "w");
    
    struct tree *root = NULL; // initialize root to NULL

    for(int Big=1;Big<=2;Big++){
        double NBig = 1000*Big;
        int* array = generate_random_array(NBig); //List of randome numbers
        for (int g=0;g<=1000*Big;g++){
                printf("%d\n",array[g]);
        }
        printf("lkj");

        return 0;

    }
}
