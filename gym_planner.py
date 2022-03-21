# Program polega na dostosowaniu optymalnego planu treningowego, oraz dietetycznego dla wszystkich dni tygodnia. 
# Miłego uzytkowania :D

import json

with open("./siłownia.json") as jsonFile:
    gym_json = json.load(jsonFile)
    jsonFile.close()

repeat = "tak"

def training_plan():
    print()
    print("Wpisz dzień tygodnia o który chodzi (poniedziałek, wtorek, środa...): ")
    a = input("")
    if a != 0:
        if a == 'poniedziałek':
            b=0
        if a == 'wtorek':
            b=1
        if a == 'środa':
            b=2
        if a == 'czwartek':
            b=3
        if a == 'piątek':
            b=4
        if a == 'sobota':
            b=5
        if a == 'niedziela':
            b=6
        print(gym_json[b]["opis"])  
        if gym_json[b]["treningowy"] == 'tak':
            print("partia ciała:",gym_json[b]["partia ciała"])
            print("ćwiczenia:",gym_json[b]["ćwiczenia"])
            print("co wypić po treningu:",gym_json[b]["po treningu"])
        else:
            print("co wypić dla najlepszego efektu:",gym_json[b]["po treningu"])

def training_day():
    print()
    print("Odzywki na dzień treningowy, wypij podane suplementy: Kreatyna x1 , białko x2 , BCAA 1x")
    print()

def wo_training_day():
    print()
    print("Odzywki na dzień bez treningu, wypij: białko x2 , kreatyna 1x")
    print()

def light_training():
    print()
    print("Odzywki na dzień z lekkim treningiem, wypij: białko 1.5 porcji, kreatyna x1")
    print()

def show():
    list = []
    print("")
    print(" Optymalny trening na siłowni by Czarek Lechowicz")
    print(" 1. Plan treningowy na cały tydzień.")
    print(" 2. Odzywki na dzień treningowy.")
    print(" 3. Odzywki na dzień bez treningu.")
    print(" 4. Odzywki na dzień z delikatnym treningiem.")
    print(" Wybierz numer:")
    c = input("") 
    if c != '0':
        if c == '1':
            list = training_plan()
        elif c == '2':
            list = training_day()
        elif c == '3':
            list = wo_training_day()
        elif c == '4':
            list = light_training()
        else:
            print("Wprowadziłeś niepoprawną nazwę, wpisz 'tak' a następnie wpisz polecenie jeszcze raz")

    jeszcze_raz = input("Czy chcesz sprawdzić jeszcze raz? Wpisz 'tak' ")

while True:
    show()

while repeat == "tak":
    show()

print()
print("Dziękujemy za skorzystanie z programu 'optymalny trening na siłowni by Czarek Lechowicz. :D ")








