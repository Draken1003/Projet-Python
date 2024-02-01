from tkinter import *


root = Tk()
root.geometry("300x500")

global liste_course
liste_course = {}
# Initialisation de la variable de suivi
variable_suivi = StringVar()

def nombre_fois(element):
    global liste_course
    if element in liste_course:
        liste_course[element] +=1
    else:
        liste_course[element] = 1
    return liste_course[element]

def ajouter_element():
    global liste_course

    element = ajouter.get()
    
    # Mettre à jour la variable de suivi
    variable_suivi.set(nombre_fois(element))

    # Rafraîchir l'affichage
    update_display(element)

def update_display(element):
    cadre = Frame()
    
    # Utiliser la variable de suivi pour obtenir le nombre de fois
    nb_fois = Label(cadre, text=variable_suivi.get())
    
    # Si l'élément est déjà dans la liste, afficher le nombre de fois
    if element in liste_course:
        nb_fois.pack(side="left")
    else:
        nb_fois.pack(side="left")
    
    Label(cadre, text=element).pack(side="left")
    Checkbutton(cadre).pack(side="right")
    
    cadre.pack()

# Exemple d'utilisation


ajouter = Entry(root)
ajouter.pack()

bouton_ajouter = Button(root, text="Ajouter", command=ajouter_element) 
bouton_ajouter.pack()

root.mainloop()