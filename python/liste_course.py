from tkinter import *

fe = Tk()
fe.geometry("300x500")


liste_course = {}

ajouter = Entry(fe)
ajouter.pack()

def nombre_fois(element):
    if element in liste_course:
        liste_course[element] +=1
    else:
        liste_course[element] = 1
    return liste_course[element]

def ajouter_element():
    element = ajouter.get()
    cadre = Frame()
    nb_fois= Label(cadre) 
    if element in liste_course:
        nb_fois.configure(text=nombre_fois(element))
        cadre.pack()
    else:
        nb_fois.configure(text=nombre_fois(element))
        nb_fois.pack(side="left")
        Label(cadre, text=element).pack(side="left")
        Checkbutton(cadre).pack(side="right")
        cadre.pack()
        
valider = Button(fe, text="Valider", command=ajouter_element) 
valider.pack()

fe.mainloop()