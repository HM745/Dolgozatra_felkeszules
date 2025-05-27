import random
brum = int(input("Adj meg egy számot (1, 2 vagy 3): ")) #Bekér egy egész számot
while brum not in (1, 2, 3): #Folyamatosan ismétlödik a ciklus amíg nem 1,2 vagy 3 a bekért adat.
    brum = int(input("Hibás! Csak 1, 2 vagy 3 lehet: ")) #Bekér egy egész számot ismét, de csak akkor ha a előző bekért adat nem 1,2 vagy 3 volt. 
else: 
    print("Helyes válasz")

def kerekites(): 
    print(round(3.1, 2)) #Kerekít 2 tizedes jegyre. Attól függ hány tizedes jegyre kerekít, hogy 3.1, után milyen szám van írva.

def for_in_range():
    print(f"*"*6, end="") #Kíirja 6x a adott adatot, majd a end egy sorba rakja.
    for i in range(2): #Kiírja 2x az adott dolgot ami utána van írva.
        print("")
        print("*    *")
    print(f"*"*6, end="")

def list():
    szamok = [] #Üres lista
    szamok.append(4) #Berak a listába egy számot.
    szamok.append(2)
    szamok.append(7)
    print(szamok)
    db = len(szamok) #Kiírja a listában szereplő számok darab számát.
    osszeg = sum(szamok) #Össze adja a listában szereplő számokat.

    print(db)
    print(osszeg)

    szamok1 = szamok[0] #Kiírja a első számot a listában.
    print(szamok1)
    szamok2 = szamok[1] #Kiírja a második számot a listában.
    utolso_szamok = szamok[len(szamok)-1] #Kiírja az utolsó számot a listában.
    print(utolso_szamok)

def ha(): 
    nem_egyenlo = 5
    if nem_egyenlo != 3: #Nem egyenlő. 
        print("semmi")
    vizsgalat = 7
    if vizsgalat == 6:
        print("semmi2") #Megvizsgálja egyenlő-e.

def formazott_kiiras():
    szam = 12
    print(f"Szám:{szam}, Dupla: {2*szam}, Gyök: {szam**0.5:.2f}") #Lehetővé teszi, hogy "" belül változokat rakjunk bele vagy műveleteket csináljunk. A:.2f 2 tizedes jegyre kerekít.

def lebego_pontos():
    szam = float(input("Lebegő pontos szám")) # Ez azért hasznos, mert így tud a program tört számot bekérni.
    print(szam)

def sortores():
    print("sortörés\nsortörés2") #Ahova rakod a \n-t ott lesz a sortörés.
