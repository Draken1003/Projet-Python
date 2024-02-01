def recherche(element,tab):
    debut = 0
    fin = len(tab) -1
    while debut <= fin:
        milieu = (debut + fin)//2
        if tab[milieu] == element:
            return True
        elif tab[milieu] > element:
            fin = milieu -1
        else:
            debut = milieu+1
    return False

from random import randint

nb_teste = 100
for nombre_teste in range(0,nb_teste):
    e = randint(-1000,1000)
    tableau = [randint(-1000,1000) for i in range(0,randint(1,100))]
    tableau.sort
    try :
        assert recherche(e,tableau) == (e in tableau)
        print("teste n", nombre_teste, "ok")
    except:
        print("teste n", nombre_teste, "echouer")