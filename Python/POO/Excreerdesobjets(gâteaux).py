class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def cut_cake(self,parts):
        if self.flavor == "chocolate":
            print(f"the cake {self.flavor} is shared in {parts} parts")
        elif self.flavor == "banana":
            print(f"the cake flavor is banana and is slice in {parts} parts")
        else:
            print(f"the cake flavor may be vanilla or mango")

#j'instance l'objet cake banane
cake = Cake("banana")
cake.cut_cake(8)
