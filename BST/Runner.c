#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    
    FILE* file = fopen("Wyniki.txt", "a");
    
    for(int Big=1;Big<=30;Big++){

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

        /////////////////List Creation//////////////////////////
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
        /////////////////////////////////////////////////////////////

        //////////////////LIST SERCH//////////////////////////////////
        fprintf(file,"List serch time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");

        printf("Starting runner for List serching: \n");
                // start timer
        QueryPerformanceCounter(&t1);
        
        for(int i=0;i<NBig;++i){
                Serch(lista,array[i]);
        }
        
        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);
        /////////////////////////////////////////////////////////////


        /////List Deletion///////////////////////////
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
        /////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////////////////////
                //List //Tree //Line //
/////////////////////////////////////////////////////////////////////////////////////////

        /////////////////Tree Creation///////////////////////
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
        /////////////////////////////////////////////////////////////

        ////////////Tree Serch//////////////////////////////////////
        fprintf(file,"Tree Search time on run nr : ");
        fprintf(file,"%d",Big);
        fprintf(file," : ");
        printf("Starting runner for Tree searching: \n");
        
                // start timer
        QueryPerformanceCounter(&t1);
        
        for(int i=0;i<NBig;++i){
                search(root,array[i]);
        }
        QueryPerformanceCounter(&t2);
        elapsedTime = (t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart; //timer end
        fprintf(file, "%f\n", elapsedTime);

        //////////////////////////////////////////////////////////////

        //////////////////////Tree Deletion////////////////////////
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
        /////////////////////////////////////////////////////////////


        }
        fclose(file);
        return 0;

}
