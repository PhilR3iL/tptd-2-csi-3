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

fichier_existe()