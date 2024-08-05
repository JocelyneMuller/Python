class User:
    def __init__(self, name):
        self.name = name

def subscribe(self):
    pass


class Moderator:
    def __init__(self, identity):
        self.identity = identity

    def modify_a_post(self):
        pass


class DiscussionThread:
    def __init__(self, title):
        self.title = title(titlestring)
    
    def add_post(self):
        pass


class Post:
    def __init__(self,date,name_of_user,text,file):
        self.date = date
        self.name_of_user = name_of_user
        self.text = text
        self.file = file
        
    
    def display(self):
        print(f"On {self.date}, {self.name_of_user} share a post {self.text} with a file {self.file}. Would you like to comment, share it? ")



class PostWithFile:
    def __init__(self, type_of_file):
        self.type_of_file = type_of_file 
    
    def show_file(self):
        pass
    

class File:
    def __init__(self, type_of_file, name, size):
        self.type_of_file = type_of_file
        self.name = name
        self.size = size
    
    def display(self):
        print(f"le fichier est : {self.type_of_file}")


class ImageFile:
    def __init__(self, type_of_file):
        self.type_of_file =  type_of_file
    
    def display(self):
        print(f"le fichier est : {self.type_of_file}")
        

#J'instance ma class Post 
post = Post("5/8/2024", "JO","nouvelle recette de layer cake au citron pour le mariage de ma copine, \
            le mois dernier. Les mariés ont kiffé!!!","25Mb")


print(post.date)
post.display()

#je crée la classe GIF qui est une classe fille de la classe ImageFile

class Gif(ImageFile):
    def __init__(self,type_of_file):
        self.type_of_file = type_of_file

#j'appelle la méthode pour afficher le type de l'image 

    def display(self):
        print(f"le fichier chargée est :{self.type_of_file} " )
        


#je crée la classe JPEG qui est une classe fille de la classe ImageFile

class Jpeg(ImageFile): 
    def __init__(self,type_of_file):
        self.type_of_file = type_of_file

#j'appelle la méthode pour afficher le type de l'image 

    def display(self):
        print(f"le fichier chargée est :{self.type_of_file} " )

gif = Gif("GIF")
jpeg = Jpeg("JPEG")
gif.display()
jpeg.display()

