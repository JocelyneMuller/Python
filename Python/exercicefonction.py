salaire_mensuel = input("veuillez renseigner votre salaire mensuel : le nombre doit être entier et sans virgule")
nombre_heures_hebdomadaire = input("veuillez renseigner votre nombre d'heures hebdomadaire : ce nombre doit être entier et sans virgule")
print(salaire_mensuel)
print(nombre_heures_hebdomadaire)

#calculer le volume d'heures mensuel

def volume_horaire_mensuel(nombre_heures_hebdomadaire,nombre_de_semaines):
    resultat = nombre_heures_hebdomadaire * nombre_de_semaines
    return resultat

nombre_heures_hebdomadaire
nombre_de_semaines = 4
nombre_heures_mensuel = volume_horaire_mensuel(nombre_heures_hebdomadaire,nombre_de_semaines)
print(nombre_heures_mensuel)

def salaire_horaire(salaire_mensuel,nombre_heures_mensuel):
    resultat = salaire_mensuel / nombre_heures_mensuel
    print(resultat)

salaire_horaire("le salaire horaire est de:", salaire_mensuel,nombre_heures_mensuel)