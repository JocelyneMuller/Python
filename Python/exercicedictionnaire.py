fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
    }
#fruits["kiwi"] = "vert"
#fruits.update({"kiwi" : "vert"})
#print(fruits)
#fruits["couleur_banane"] = fruits.get("banane")
#fruits["pomme"] = "vert"
#del fruits["orange"]
#print(fruits)
# 6. Affichage des clés restantes dans le dictionnaire
#print(fruits.keys())
for fruit in fruits:
    print(fruit)
else:
    print("plus de fruit dans le panier, il est temps de faire les courses")