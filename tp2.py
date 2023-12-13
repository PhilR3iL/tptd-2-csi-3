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

print(sinc(0))
