import os
from random import randrange
from time import sleep

antwoord = ""
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
    os.system("cls")
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
    antwoord = input("walk or fletnix :")
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
    os.system("cls")
    print("you sneak on a cargo ship")
    option = randrange(1,5)
    if option == 1:
        os.system("cls")
        sneak_s_f()
    else:
        os.system("cls")
        print("you get caught sneaking an are ejected of the ship and your blood expands rupturing your veins")

def sneak_s_f():
    print("you arive at Nedera you go to the land of amsterdam and you did not get caught\nyou still have some money and you are free to roam around.\nbut it is only half of the amount tor a visum so do you either find a job or take a free dutch class at the library")
    antwoord = input("job or dutch :")
    if antwoord == "job":
        os.system("cls")
        job()
    elif antwoord == "dutch":
        os.system("cls")
        dutch()

def job():
    job = randrange(0,2)
    print("what job do you want a pool cleaner or a postman")
    antwoord = input("pool or postman")
    if antwoord == "pool" and job == 0:
        os.system("cls")
        print("you get a job as a pool cleaner")
        print("working...")
        sleep(3)
        print("after 2 months of hard work you finaly get enouch money for a visum\nand you won is was the second way")
    elif antwoord == "postman" and job == 1:
        os.system("cls")
        print("you get a job as postman")
        print("working...")
        sleep(3)
        print("after 2 months of hard work you finaly get enouch money for a visum\nand you won is was the second way")
    elif antwoord == "postman" and job == 0:
        print("thay turned you down becouse you dont speak dutch\nyou can now only beg or take free dutch classes since you have no money")
        antwoord = input("beg or dutch")
        if antwoord == "beg":
            os.system("cls")
            beg()
        elif antwoord == "dutch":
            os.system("cls")
            dutch_2()
    elif antwoord == "pool" and job == 1:
        print("thay turned you down becouse you dont speak dutch")
        antwoord = input("beg or dutch")
        if antwoord == "beg":
            os.system("cls")
            beg()
        elif antwoord == "dutch":
            os.system("cls")
            dutch_2()

def dutch():
    print("you take dutch classes")
    print("learning...")
    sleep(3)
    print("je hebt nu een examen")
    antwoord = input("wat betekent \"ik weet het niet\" :")
    if antwoord == "i dont know":
        job_3()
    else:
        print("you fail but you can stil aply for a job")
        job_4()

def dutch_2():
    print("since you have little to no money you cant afford your painkillers anymore\nyou start using cheap but adictive painkillers but you still try to learn dutch")
    print("learning...")
    sleep(3)
    print("je hebt nu een examen")
    antwoord = input("wat betekent \"ik weet het niet\" :")
    if antwoord == "i dont know":
        job_2()
    else:
        print("you fail so your last resort is begging")
        beg()

def job_2():
    kans = randrange(0,2)
    print("now with the ability to fluently speak dutch it chould be much more easy to find a job/ndo you become a taxi driver or a bartender")
    antwoord = input("driver or bartender")
    if antwoord == "driver" and kans == 1:
        print("you got the job as taxi driver\ndriving...")
        sleep(3)
        print("after telling countless pouple yout lifestory you finaly have enouch money for a visum")
    elif antwoord == "bartender" and kans == 0:
        print("you got the job as bartender\ntending bars")
        sleep(3)
        print("after making a lot of martinis  you finaly have enouch mo9ney for a visum")

def job_3():
    print

def job_4():
    print

def beg():
    print("you enter a crippeling depression while beggins and you get adicted to drugs and alcehol")
    kans = randrange(1,10)
    if kans == 1:
        print("while begging by central station of amsterdam you encounter mr beast and he gives you 100 Milion euro")

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