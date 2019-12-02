from random import randint
import json
from datetime import datetime

class Result:
    def __init__(self, score, player_name, date):
        self.player_name = player_name
        self.score = score
        self.date = date

def game(zacetno, koncno):
    skrito = randint(zacetno, koncno - 1)
    print(zacetno, skrito, koncno)
    izbrana_stevilka = -1
    isTrue = False
    seznam_ugibanj = []
    while izbrana_stevilka!=skrito:
        if isTrue == True:
            print("Žal vaša številka ni prava. Poskusite znova.")
        izbrana_stevilka = vprasaj_stevilko()
        isTrue = True
        seznam_ugibanj.append(izbrana_stevilka)
    print("Čestitam! Zadeli ste skrito število!")
    
    return seznam_ugibanj

def vprasaj_stevilko():
    stevilka = int(input("Izberi številko med 1 in 100\n"))
    return stevilka

def zapisi_v_datoteko(igralec):
    with open("results.txt", "a") as output_file:
        niz = json.dumps(igralec.__dict__)
        output_file.write(niz+"\n")

def vprasaj_osebo():
    return input("Napiši svoje ime:\n")

if __name__ == "__main__":
    isTrue = True
    while isTrue:
        ime_osebe = vprasaj_osebo()
        ugibanja = game(1, 100)
        #print(ugibanja)
        date_now = datetime.now()
        date = date_now.strftime("%d/%m/%Y, %H:%M:%S")
        igralec = Result(ugibanja, ime_osebe, date)
        zapisi_v_datoteko(igralec)
        nova_igra = input("Želiš igrati še enkrat? (Da/Ne)\n")
        nova_igra = nova_igra.upper()
        if nova_igra == "NE":
            isTrue = False
        elif nova_igra == "DA":
            isTrue = True
