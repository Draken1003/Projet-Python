from tkinter import *

fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("compteur de mot ")

entre_mot = Entry(fenetre)
entre_mot.pack()

entre_lettre = Entry(fenetre)
entre_lettre.pack()

nombre_lettre = Label(fenetre, text= "" )
nombre_lettre.pack()

def comptage_de_lettre():
    c=0
    lettre_a_chercher= entre_lettre.get()
    for l in entre_mot.get().lower():
        if l== lettre_a_chercher:
            c+=1
    nombre_lettre.config(text=c)

accepter = Button(fenetre, text = "Accepter" , command= comptage_de_lettre)
accepter.pack()

fenetre.mainloop()