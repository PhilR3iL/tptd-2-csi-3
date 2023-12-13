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

print("Vous avez ", age(), " ans.")
