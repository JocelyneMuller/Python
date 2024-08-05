liste_nombres = input("entrez une liste de quatre nombres entiers séparés par des virgules :")
liste =  liste_nombres.split(",")

#initialiser la somme à 0
somme = 0

#clacluler la somme en parcourant la liste
for nombre in liste:
    somme += int(nombre)
print("la somme est égal à :", somme)

#calcul de la moyenne
moyenne = somme/len(liste)
print("la moyenne est égale à:", moyenne)

#Trouver les nombres supérieurs à la moyenne
nombres_superieurs = 0
while nombres_superieurs > moyenne :
    print(nombres_superieurs)
print(nombres_superieurs)