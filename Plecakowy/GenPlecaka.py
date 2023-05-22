import random

Rozmiar = 10
IloscPrzedmiotów = 20

Plecak=[]
Wagi=[]
Koszt=[]

def GenPrzedmioty():
    global Wagi,Koszt,IloscPrzedmiotów
    for i in range(IloscPrzedmiotów):
        r=10
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



if __name__ =="__main__":
    GenPrzedmioty()
    
    print("Wagi",Wagi)
    print("Koszt",Koszt)

    print("Rozmiar",Rozmiar)
    Zachłanny()

    print("-------")
    print(Plecak)