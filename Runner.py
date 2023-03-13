import time
import Sorting
import RandNum
import sys
import Numbers
sys.setrecursionlimit(2000000)

f = open("wyniki.txt","w")

cat=[lambda x: Sorting.insertSort(x), lambda x: Sorting.selectionSort(x),lambda x: Sorting.mergeSort(x),lambda x: Sorting.heapSort(x)]
cat2=["insert","selection","merge","heap"]
cat3=["Ones","Ascending","Descending","Random","A_Shape","V_Shape"]

Ones=Numbers.Ones
Ascending = Numbers.Ass
Descending = Numbers.Des
Random = Numbers.Rand

for g in range(6):
    print(cat3[g])
    f.write(cat3[g]+"\n")

    for j in range(4):
        print('Sorting:',cat2[j])
        f.write('Sorting:'+str(cat2[j])+"\n")

        run=1
        for i in range(1,16):

            if g==0:
                Le=(1000*i)
                tab=Ones[1:Le]
            if g==1:
                Le=(1000*i)
                tab=Ascending[1:Le]
            if g==2:
                Le=(1000*i)
                tab=Descending[1:Le]
            if g==3:
                Le=(1000*i)
                tab=Random[1:Le]
            if g==4:
                tab=Numbers.ShapeA(1000*i)
            if g==5:
                tab=Numbers.ShapeV(1000*i)
            
            startTime = time.time_ns() #time at start

            cat[j](tab)
            
            endTime= time.time_ns()    #time at end #NANO MACHINES SON !
            totalTime= endTime - startTime  #run time
            
            print(run,'Total run time in nanoseconds =',(totalTime))    #display run time
            
            f.write(str(run)+":"+"Total run time in nanoseconds ="+str(totalTime)+"\n")
            
            run+=1
            del(tab)
            
    print("\n")
    f.write("\n")

f.close()