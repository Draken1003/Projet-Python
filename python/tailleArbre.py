import turtle

def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre[1]) + taille(arbre[2])


arbre = [1, [2, [4, None, None], [5, None, None]], [3, None, None]]

# Calcul de la taille de l'arbre
taille_arbre = taille(arbre)
print("La taille de l'arbre est :", taille_arbre)

