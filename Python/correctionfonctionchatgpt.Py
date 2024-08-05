# Demander les entrées à l'utilisateur
salaire_mensuel = input("Veuillez renseigner votre salaire mensuel : le nombre doit être entier et sans virgule ")
nombre_heures_hebdomadaire = input("Veuillez renseigner votre nombre d'heures hebdomadaire : ce nombre doit être entier et sans virgule ")

# Convertir les entrées en entiers
try:
    salaire_mensuel = int(salaire_mensuel)
    nombre_heures_hebdomadaire = int(nombre_heures_hebdomadaire)
except ValueError:
    print("Veuillez entrer des nombres entiers valides.")
    exit()

# Afficher les valeurs entrées
print(f"Salaire mensuel : {salaire_mensuel}")
print(f"Nombre d'heures hebdomadaire : {nombre_heures_hebdomadaire}")

# Calculer le volume d'heures mensuel
def volume_horaire_mensuel(nombre_heures_hebdomadaire, nombre_de_semaines):
    resultat = nombre_heures_hebdomadaire * nombre_de_semaines
    return resultat

nombre_de_semaines = 4
nombre_heures_mensuel = volume_horaire_mensuel(nombre_heures_hebdomadaire, nombre_de_semaines)
print(f"Volume horaire mensuel : {nombre_heures_mensuel}")
