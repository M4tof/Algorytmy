import time
import Sorting

tab=[9,7,5,3,1,8,6,4,2,0,1011,22,123,1243,4244,2333,333,22,121,22,5,87,4]

startTime = time.time() #time at start

print(Sorting.insertSort(tab))

endTime= time.time()    #time at end
totalTime= endTime - startTime  #run time
print(totalTime)    #display run time