#def afficher_message():
    #print("Bonjour Paris")

#afficher_message()

#def afficher_nom_et_prenom(nom, prenom, age):
    #print("le nom est:", nom)
    #print("le prénom est:", prenom)
    #print("l'âge est:", 30)

#afficher le nom, prénom et âge grâce à une fonction
#afficher_nom_et_prenom("Poualeu", "Jocelyne", "30")
#def afficher_nom_et_prenom(nom, prenom, age):
    #print("le nom est:", nom)
    #print("le prénom est:", prenom)
    #print("l'âge est:", 30)
#afficher_nom_et_prenom("Poualeu", "Jocelyne", "30")

#effectuer l'addition de deux valeurs grâce à une fonction
#def addition(a,b):
    #resultat = a+b
    #print(resultat)

#addition(20,30) avec la fonction avec paramètres

#def addition(a,b):
    #resultat = a+b
    #print(resultat)

#param1 = 20
#param2 = 30
#addition(param1,param2)

#addition(20,30) avec la fonction de retour

def addition(a,b):
    resultat = a+b
    return resultat
#return est un mot clé pour afficher le résultat de l'addition
param1 = 20
param2 = 30
#retour est une nouvelle variable qui stocke la valeur de la fonction addition
retour = addition(param1,param2)
print(retour)
