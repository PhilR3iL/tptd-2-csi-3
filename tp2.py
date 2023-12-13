def age() -> int:
    continuer = True
    while continuer:
        age = input("Entrez votre âge : ")
        try:
            age = int(age)
            continuer = False
        except ValueError:
            print("Entrez un chiffre !")
    return age

# print("Vous avez ", age(), " ans.")

#################################################

from math import sin

def sinc(x : float) -> float:
    try:
        return sin(x)/x
    except ZeroDivisionError:
        return 1

#print(sinc(0))

#####################################

def fichier_existe():
    continuer = True
    while continuer:
        nom_fichier = input("Entrez un nom de fichier : ")
        try:
            open(nom_fichier)
            continuer = False
        except FileNotFoundError:
            print("Le fichier n'existe pas.")

#fichier_existe()

#############################################

import random
import time

def un_petit_jeu():
    x = random.randint (0 ,100)
    print("Vous devez arrêter le programme sur %d." % x)
    print("Pour arrêter le programme, il faut faire Ctrl+C.")
    print("Appuyer sur Entrée pour commencer...")
    b = input()
    i = 0
    try:
        while (i < 100) :
            i+=1
            print("%d\x0d" % i)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Le programme a été interrompu par l'utilisateur.")
    if i == x:
        print("Vous avez gagné.")
    else:
        print("Vous avez perdu.")    

#un_petit_jeu()

####################################
def pente(xA : float, yA : float, xB : float, yB : float) -> float:
    try:
        result = (yB - yA) / (xB - xA)
        return result
    except:
        return "la droite est verticale"

print(pente(2, 5, 4, 1))
