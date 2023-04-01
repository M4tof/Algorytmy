       
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