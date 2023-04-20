#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <windows.h>
#include "Functions.c" 

int main(){
    
    FILE* file = fopen("Wyniki.txt", "a");
    
    for(int Big=1;Big<=1;Big++){

        double NBig = 7*Big;

        int array[7] = {1,2,4,3,5,10,9}; //List of randome numbers
    
        LARGE_INTEGER frequency;        // ticks per second
        LARGE_INTEGER t1, t2;           // ticks
        double elapsedTime;
        // get ticks per second
        QueryPerformanceFrequency(&frequency);

        //Dla tablicy
        
        printf("Run nr: ");
        printf("%d\n",Big);

/////////////////////////////////////////////////////////////////////////////////////////
                //List //Tree //Line //
/////////////////////////////////////////////////////////////////////////////////////////

        /////////////////Tree Creation///////////////////////
        struct tree *root = NULL; // initialize root to NULL
            
        for(int i=1; i<=NBig; i++){
            root = insert(root, array[i]);
        }
        /////////////////////////////////////////////////////////////

        ////////////Tree Serch//////////////////////////////////////

        for(int i=0;i<NBig;++i){
                printf("%d ==> ",array[i]);
                printf("%d\n",search(root,array[i]));
        }

        //////////////////////////////////////////////////////////////

        //////////////////////Tree Deletion////////////////////////

        DeleteTree(root);

        /////////////////////////////////////////////////////////////

        }
        fclose(file);
        return 0;

}
