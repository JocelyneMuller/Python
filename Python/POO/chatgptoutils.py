class MaClasse:
    def __init__(self):
        # Initialise une liste vide
        self.ma_liste = []

    def ajouter_element(self, element):
        # Utilise la méthode append pour ajouter l'élément à la liste
        self.ma_liste.append(element)
        print(f"Élément {element} ajouté à la liste.")

    def afficher_liste(self):
        # Affiche tous les éléments de la liste
        print("Contenu de la liste :")
        for element in self.ma_liste:
            print(element)

# Création d'une instance de MaClasse
ma_instance = MaClasse()

# Ajouter des éléments à la liste
ma_instance.ajouter_element("Pomme")
ma_instance.ajouter_element("Banane")
ma_instance.ajouter_element("Cerise")

# Afficher le contenu de la liste
ma_instance.afficher_liste()
