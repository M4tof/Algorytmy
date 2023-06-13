import random
import time

Rozmiar = 10000  #How much can be stored in the backpack
IloscPrzedmiotów = 10000  #How manny iteams are taken into consideration

Plecak=[]   #Backpack
Wagi=[]     #Sizes of iteams
Koszt=[]    #Values of iteams

def ClearData():
    global Plecak,Wagi,Koszt
    Plecak=[]   #Backpack
    Wagi=[]     #Sizes of iteams
    Koszt=[]    #Values of iteams

def GenPrzedmioty():
    global Wagi,Koszt,IloscPrzedmiotów
    for i in range(IloscPrzedmiotów):
        
        r=1000                  #Maks arithemtic value of size and value
        
        Wagi.append(random.randint(1,r))
        Koszt.append(random.randint(1,r))

def Zachłanny():
    global Plecak,Wagi,Koszt,Rozmiar,IloscPrzedmiotów

    Temp=[]
    Włożone=0

    for j in range(IloscPrzedmiotów):
        Temp.append([Koszt[j]/Wagi[j],Koszt[j],Wagi[j]])

    Temp.sort(key = lambda x: (x[0]))
    Temp=Temp[::-1]
    #print(Temp)
    for i in range(IloscPrzedmiotów):
        if Temp[i][2] + Włożone <= Rozmiar:
            Włożone += Temp[i][2]
            Plecak.append(Temp[i][1])

def Dynamiczny():
    global Plecak,Wagi,Koszt,Rozmiar,IloscPrzedmiotów
    Tablica = [[0] * (Rozmiar + 1) for _ in range(IloscPrzedmiotów + 1)]
    
    for i in range(1,IloscPrzedmiotów+1):
        for j in range(1,Rozmiar+1):
            if Wagi[i-1] <= j:
                Tablica[i][j] = max(Tablica[i - 1][j], (Tablica[i - 1][j - Wagi[i - 1]] + Koszt[i - 1] ))
            else:
                Tablica[i][j]=Tablica[i-1][j]
    
    #print(Tablica)
    i = IloscPrzedmiotów
    j = Rozmiar
    while i > 0 and j > 0:
        if Tablica[i][j] != Tablica[i - 1][j]:
            Plecak.append(Koszt[i - 1])
            j -= Wagi[i - 1]
        i -= 1

    Plecak.reverse()
    #print(Plecak)


file = open("wyniki.txt","a")


for j in range(10):
    if __name__ =="__main__":
        for i in range(1,16):
            Rozmiar = 1000*i
            #IloscPrzedmiotów = i*100

            GenPrzedmioty()
                
                # print("Wagi",Wagi)
                # print("Koszt",Koszt)

                # print("Rozmiar",Rozmiar)
                
            Zachłanny()


            print("-------Zachłanny-------")
            print(Plecak, "=>", sum(Plecak))
                
            A=sum(Plecak)
            
            Plecak=[]

            Dynamiczny()


            print("-------Dynamiczny-------")
            print(Plecak, "=>", sum(Plecak))

            B=sum(Plecak)

            Blad = (B-A)/B 
                
            file.write("Blad,"+str(i)+","+str(Blad)+"\n")
                
            ClearData()


file.close()