import time
import Sorting
import RandNum
from time import sleep
from threading import Timer

tab=RandNum.RandGen()

startTime = time.time() #time at start
#############################################CODE BLOCK####################

#tab=Sorting.sleepSort(tab)
#Sorting.insertSort(tab)
#Sorting.selectionSort(tab)
#Sorting.mergeSort(tab)
#Sorting.quickSort(tab,0,(len(tab)-1))

print(tab)

#############################################CODE BLOCK####################
endTime= time.time()    #time at end
totalTime= endTime - startTime  #run time
print('Total run time =',(totalTime))    #display run time
