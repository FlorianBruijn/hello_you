import os
from time import sleep

feul = False
antwoord = ""
begun = 0
os.system("cls")

def start():
    print("you are flying home after a long day of astroid mining when you see your almost out of feul but you will make it home\ndo you refeul?")
    antwoord = input("yes or no :")
    if antwoord == "yes":
        refeul()
    elif antwoord == "no":
        os.system("cls")
        a()
    else:
        os.system("cls")
        print("type yes or no")
        start()

def refeul():
    feul = True
    os.system("cls")
    print("refeuling...")
    sleep(3)
    print("tank full")
    a_f()

def a_f():
    print("upon ariving at your home planet, Aroda you get stopped by a customs spaceship.\nhe searches yous spaceship becous of rizing threats of terrorists from planet grimfar.")
    print("after he searches your ship you are hungry\ndo you eat at home or at burgerqueen")
    antwoord = input("home or burger :")
    if antwoord == "home":
        os.system("cls")
        home_f()
    elif antwoord == "burger":
        os.system("cls")
        print("after you eat your burger and get back on your spaceship you see a distant flash and after a few seconds hear a ear bursting bang")
        burger_f()

def home_f():
    print("when you get home you eat some pancakes\nafter dinner do you go for a walk or do you wach fletnix")
    antwoord = input("walk or fletnix")
    if antwoord == "walk":
        os.system("cls")
        print("after some time of walking you heat a loud bang")
        burger()
    elif antwoord == "fletnix":
        os.system("cls")
        fletnix_f()

def fletnix_f():
    print("you wach a history show about WW6, \nand just as a planet gets destroid by a antimatter nuke you get knocked out")
    print("you later wake up in a hospital bed. \nyou ask a doctor where you are and he tels you you are in a hospital on wrendaft")
    print("he tells you you are lucky you survived")
    print("after 2,5 months you get dismissed from the hospital with a prescription of heavy painkillers and no ship")

    print("you are low on money becouse u refeuled your ship\nyou can pay a cheap smuggler or sneak on a cargo plane")
    antwoord = input("smuggle or sneak :")
    if antwoord == "sneak":
        os.system("cls")
        sneak_f()
    elif antwoord == "smuggle":
        os.system("cls")
        smuggle_f()

def sneak_f():
    print

def smuggle_f():
    print

def burger_f():
    print

def a():
    print("upon ariving at your home planet, Aroda you get stopped by a customs spaceship.\nhe searches yous spaceship becous of rizing threats of terrorists from planet grimfar.")
    print("after he searches your ship you are hungry\ndo you eat at home or at burgerqueen")
    antwoord = input("home or burger :")
    if antwoord == "home":
        os.system("cls")
        home()
    elif antwoord == "burger":
        os.system("cls")
        print("after you eat your burger and get back on your spaceship you see a distant flash and after a few seconds hear a ear bursting bang")
        burger()

def home():
    print("when you get home you eat some pancakes\nafter dinner do you go for a walk or do you wach fletnix")
    antwoord = input("walk or fletnix")
    if antwoord == "walk":
        os.system("cls")
        print("after some time of walking you heat a loud bang")
        burger()
    elif antwoord == "fletnix":
        os.system("cls")
        fletnix()

def fletnix():
    print("you wach a history show about WW6, \nand just as a planet gets destroid by a antimatter nuke you get knocked out")
    print("you later wake up in a hospital bed. \nyou ask a doctor where you are and he tels you you are in a hospital on wrendaft")
    print("he tells you you are lucky you survived")
    print("after 2,5 months you get dismissed from the hospital with a prescription of heavy painkillers and no ship")
    print("you have just enouch money fur a cheap cruis to nedera or do you go with a cheap smuggler or by sneaking on a cargo ship")
    
    antwoord = input("smuggle or sneak or cruise :")
    if antwoord == "sneak":
        os.system("cls")
        sneak()
    elif antwoord == "smuggle":
        os.system("cls")
        smuggle()
    elif antwoord == "cruise":
        os.system("cls")
        cruise()

def cruise():
    print

def smuggle():
    print

def sneak():
    print

def burger():
    print

start()