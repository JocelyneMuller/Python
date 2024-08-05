#créer la class toolbox

class ToolBox:
    def __init__(self):
        self.tools = []
        
#je crée la méthode add pour ajouter un outil dans la boite à outils

    def add_tool(self, element):
        self.tools.append(element)
        print(f"the tool {element} have been added to my box of tools")

#je crée la méthode show pour afficher l'outil qui a été ajouté dans la boite à outils

    def show_list(self):
        print("the content of the list")
        for element in self.tools:
            print(element)

#je crée la méthode remove pour enlever les outils de ma toolbox

    def remove_tool(self, element):
            self.tools.remove(element)
            print(f"the tool {element} have been removed from my box of tools")

    def show_list(self):
        print("the content of the list")
        for element in self.tools:
            print(element)

#je crée l'instance outil de la classe ToolBox
outil = ToolBox()

#j'ajoute des éléments à ma liste
outil.add_tool("Hammer")
outil.add_tool("Screwdriver")
outil.add_tool("Screw")
outil.add_tool("nails")
outil.add_tool("meter")

#j'imprime ma liste
outil.show_list()

#je retire le marteau de ma liste
outil.remove_tool("Hammer")

#j'imprime ma liste
outil.show_list()

# créer la class hammer   

class Hammer:
    def __init__(self, color = "red"):
        self.hammer = Hammer
        self.color = color

def panting_color(self, nails):
        pass
'''peindre le marteau'''

def planting(self, nails):
        pass
'''planter des clous'''


def remove(self, nails):
        pass
'''retirer des clous'''


# créer la class screwdriver 

class ScrewDriver:
    def __init__(self, size):
        self.size = size

def tighten(self, screw):
        pass
'''serrer les vis'''

def deserrate(self, screw):
        pass
'''déserrer les vis'''