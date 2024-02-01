# Créé par hetit, le 24/09/2023 en Python 3.7
def moyenne(tab):
    coef = 0
    somme =0
    for (valeur,coefficient) in tab:
        somme += valeur*coefficient
        coef = coef + coefficient
    moyen = somme / coef
    return moyen



