file = open('data.txt')
R = file.readlines()
file.close()

tab=[]
print(R)
for i in R:
    i=list(map(int,i.strip().split()))
    print(i)