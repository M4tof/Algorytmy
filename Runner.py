import time
import Sorting
import RandNum

tab=RandNum.RandGen()

startTime = time.time() #time at start
#############################################CODE BLOCK####################

Sorting.mergeSort(tab)

print(tab)

#############################################CODE BLOCK####################
endTime= time.time()    #time at end
totalTime= endTime - startTime  #run time
print('Total run time =',totalTime)    #display run time