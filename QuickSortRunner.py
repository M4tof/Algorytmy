import time
import random
import Sorting
import RandNum
import sys
import Numbers
sys.setrecursionlimit(2000000)

def quickSortRight(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[-1]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSortRight(less)+equal+quickSortRight(greater)
    else:
        return array

def quickSortMid(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[len(array)//2]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSortMid(less)+equal+quickSortMid(greater)
    else:
        return array
    
def quickSortRand(array):
    less = []
    equal = []
    greater = []
    R = random.randint(0, len(array))
    if len(array) > 1:
        pivot = array[R-1]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSortRand(less)+equal+quickSortRand(greater)
    else:
        return array

f = open("wynikiQsort.txt","w")
f.write("Czas"+":200:400:600:800:1000:1200:1400:1600:1800:2000:2200:2400:2600:2800:3000\n")

print("Right:")
f.write("Right:")
run=1
for i in range(2,32,2):
    tab=Numbers.ShapeA(100*i)
    startTime = time.time() #time at start

    tab=quickSortRight(tab)
            
    endTime= time.time()    #time at end #NANO MACHINES SON !
    totalTime= endTime - startTime  #run time
            
    print(run,100*i,'Total run time in nanoseconds =',(totalTime))    #display run time
    f.write(str(totalTime)+":")

    del(tab)
    run+=1

f.write("\n")
f.write("Mid:")
print("Mid")
run=1
for i in range(2,32,2):
    tab=Numbers.ShapeA(100*i)
    startTime = time.time() #time at start

    tab=quickSortMid(tab)
            
    endTime= time.time()    #time at end #NANO MACHINES SON !
    totalTime= endTime - startTime  #run time
            
    print(run,100*i,'Total run time in nanoseconds =',(totalTime))    #display run time
    f.write(str(totalTime)+":")

    del(tab)
    run+=1


f.write("\n")
f.write("Rand:")
print("Rand")
run=1
for i in range(2,32,2):
    tab=Numbers.ShapeA(100*i)
    startTime = time.time() #time at start

    tab=quickSortRand(tab)
            
    endTime= time.time()    #time at end #NANO MACHINES SON !
    totalTime= endTime - startTime  #run time
            
    print(run,100*i,'Total run time in nanoseconds =',(totalTime))    #display run time\
    f.write(str(totalTime)+":")

    del(tab)
    run+=1

f.close()