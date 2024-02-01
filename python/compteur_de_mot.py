def compteur_de_mot(chaine):
    pas_mot = [' ',"'"]
    nb_mot = 1
    if len(chaine) == 0:
        return 0
    else:
        for e in chaine:
            if e in pas_mot:
                nb_mot +=1
        return nb_mot

print(compteur_de_mot("Je m'apelle helder et j'ai 17 ans"))