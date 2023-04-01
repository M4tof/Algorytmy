#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    
    FILE* file = fopen("Wyniki.txt", "w");
    
    for(int Big=1;Big<=15;Big++){

        double NBig = 1000*Big;

        int* array = generate_random_array(NBig); //List of randome numbers
    
        LARGE_INTEGER frequency;        // ticks per second
        LARGE_INTEGER t1, t2;           // ticks
        double elapsedTime;
        // get ticks per second
        QueryPerformanceFrequency(&frequency);

        //Dla tablicy
        
        printf("Run nr: ");
        printf("%d\n",Big);

        
        fprintf(file,"List Creation time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");

        
        printf("Starting runner for List creation: \n");
        
                // start timer
        QueryPerformanceCounter(&t1);

        node * lista = NULL;
        lista = (node *) malloc(sizeof(node)); //Create and Name
        
        for(int i=1; i<=NBig; i++){
            Add(lista,&lista,array[i]);
        }
        
        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);

        
        fprintf(file,"List Deletion time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");
        printf("Starting runner for List deletion: \n");
        
                // start timer
        QueryPerformanceCounter(&t1);

        DeleteList(&lista);

        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);




/////////////////////////////////////////////////////////////////////////////////////////
        fprintf(file,"Tree Creation time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");
        printf("Starting runner for Tree creation: \n");
        
                // start timer
        QueryPerformanceCounter(&t1);

        struct tree *root = NULL; // initialize root to NULL
            
        for(int i=1; i<=NBig; i++){
            root = insert(root, array[i]);
        }

        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);

        fprintf(file,"Tree Deletion time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");
        printf("Starting runner for Tree deletion: \n");
        
                // start timer
        QueryPerformanceCounter(&t1);

        DeleteTree(root);

        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);


        }
        fclose(file);
        return 0;

}
