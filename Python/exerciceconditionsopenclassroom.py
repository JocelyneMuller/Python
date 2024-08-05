nombre_a_droite=0
nombre_a_gauche=15
symbole="/"
resultat=0

match symbole:
    case "+":
        resultat = nombre_a_droite + nombre_a_gauche
    case "-":
        resultat = nombre_a_droite - nombre_a_gauche
    case "*":
        resultat = nombre_a_droite * nombre_a_gauche
    case "/":
        if nombre_a_droite == 0:
            print("Division par 0:impossible")
        else:
            resultat = nombre_a_gauche/ nombre_a_droite
    case _:
        print("Exit")
print(resultat)