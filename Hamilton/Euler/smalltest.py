    while ToDell > 0:
        Y = random.randint(0,N-1)
        if (MacierzSąsiedztwa[Y].count(1) > 1):
            while True:
                IntToDel=random.randint(0,N-1)
                if(MacierzSąsiedztwa[Y][IntToDel]==1):
                    break
            
            MacierzSąsiedztwa[Y][IntToDel]=0
            MacierzSąsiedztwa[IntToDel][Y]=0
            ToDell-=1   
    
    Nieparzyste=[]
    for y in range(n):
        if (MacierzSąsiedztwa[y].count(1))%2 == 1:
            Nieparzyste.append(y)

    while len(Nieparzyste)>2:
        Y=Nieparzyste[(random.randint(0,len(Nieparzyste)-1))]
        X=Nieparzyste[(random.randint(0,len(Nieparzyste)-1))]
        if X!=Y and MacierzSąsiedztwa[X][Y]==0:
            MacierzSąsiedztwa[X][Y]=1
            MacierzSąsiedztwa[Y][X]=1
            Nieparzyste.remove(Y)
            Nieparzyste.remove(X)