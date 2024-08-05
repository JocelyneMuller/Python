class Film:
    def __init__(self, name):
        self.name = name

#je crée la méthode visonnage qui est un comportement de la class
    def watch(self):
        print("Bon visionnage !")

#je crée la classe fille 

class FilmCassette(Film):
    def __init__(self, name, magnetic_tape = True):
        self.name = name
        self.magnetic_tape = True

#je crée la méthode rewind pour ma classe FilmCassette
    def rewind(self):
        print("c'est long à rembobiner")
        self.magnetic_tape = True

#je crée la classe fille DVD
class DVD(Film):
    def __init__(self,name, date_de_sortie):
        self.name = name
        self.date_de_sortie = date_de_sortie

#je crée la méthode display pour la classe DVD
    def display(self):
        print(f"le film : {self.name} est sortie le {self.date_de_sortie}")
        
        
#je crée la classe fille Blu_Ray
class BluRay(Film):
    pass



#j'instance mes 2 classes Film et FilmCassette
film = Film("2001 :l'odyssée de l'espace")
film_cassette = FilmCassette("Blade Runner")
dvd = DVD("Expandable","15/3/2016")
blu_ray = BluRay("Wakanda Forever")

#j'appelle l'attribut name de ma classe Film
print(film.name)

#j'appelle la méthode(le comportement) de ma classe Film
film.watch()

#j'appelle l'attribut name de ma classe fille FilmCassette
print(film_cassette.name)
print(film_cassette.magnetic_tape)

#j'appelle la méthode(le comportement) de ma classe fille FilmCassette
film_cassette.watch() #je dois enlever cette ligne si je veux qu'il print uniquement("c'est long à rembobiner")
film_cassette.rewind()

#j'appelle l'attribut name de ma classe fille DVD
print(dvd.name)

#j'appelle la méthode(le comportement) de ma classe fille DVD
dvd.watch()
dvd.display()

#j'appelle l'attribut name de ma classe fille BluRay
print(blu_ray.name)

#j'appelle la méthode(le comportement) de ma classe fille FilmCassette
blu_ray.watch()


# NB : Dans cet exemple, la classe fille hérite des attributs mais aussi des méthodes de la classe parent