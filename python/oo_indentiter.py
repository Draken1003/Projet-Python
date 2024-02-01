from random import randint

class Identite:
    def __init__(self, nom, prenom, age, taille, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        self.date_naissance = date_naissance

    def cal_age(self,annee):
        tab = self.date_naissance.split('/')
        age = (annee - int(tab[2]))
        return age

    def cal_age_a_vivre(self, annee):
        annee_aleat = randint(annee, 2096)
        age_a_vivre = annee_aleat - annee
        return age_a_vivre

Helder = Identite("Esteves", "Helder", 17, 1.72, "10/3/2006")
print(Helder.nom, Helder.prenom)  
print(Helder.cal_age_a_vivre(2023))  
