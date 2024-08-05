class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")

# Création d'une instance de la classe Product
product1 = Product("Laptop", 999.99, 10)

# Appel de la méthode display pour afficher les attributs de l'objet
product1.display()
