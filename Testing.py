tab=[]

f = open("ASS.txt","w")

f.write('[')
for i in range(1,15001):
    f.write(str(i)+',')

f.write(']')
f.close()