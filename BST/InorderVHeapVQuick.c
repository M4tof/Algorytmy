#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    
    FILE* file = fopen("Wyniki3.txt", "a");
    FILE* dummy = fopen("dump.txt","w");
    
    for(int Big=1;Big<=30;Big++){

        double NBig = 1000*Big;

        int* array = generate_random_array(NBig); //List of randome numbers
    
        LARGE_INTEGER frequency;        // ticks per second
        LARGE_INTEGER t1, t2, t3,t4;           // ticks
        double elapsedTime;
        // get ticks per second
        QueryPerformanceFrequency(&frequency);
        
        struct tree *root = NULL; // initialize root to NULL

        fprintf(file, "InorderWCreation:%d:",Big);

        QueryPerformanceCounter(&t1);    
        for(int i=1; i<=NBig; i++){
            root = insert(root, array[i]);
        }

        Dummyinorder(dummy,root);
        
        QueryPerformanceCounter(&t2);
        
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);
        
        DeleteTree(root);

        fprintf(file, "HeapSort:%d:", Big);

        QueryPerformanceCounter(&t1);
        heapSort(array, NBig);
        QueryPerformanceCounter(&t2);
        
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);


        free(array);

        printf("%d Done",Big);
        }
        fclose(file);
        return 0;

}
