from tkinter import *

fenetre = Tk() #création d'une fenetre
fenetre.title("Mon application") #titre de mon application
fenetre.iconbitmap("C:/Users/hetit/OneDrive/Images/mannette.jpg") #mettre une icon de l'application
fenetre.config(bg = "#87CEEB") #changer la couleur de fond
fenetre.geometry("1280x720") #changer la taille de la fenetre
fenetre.maxsize(1920,1080) #taille max
fenetre.minsize(840,600) #taille minimum

cadre1 = Frame(fenetre, bg = "#87CEEB")
cadre1.pack()

texte1 = Label(cadre1, text = "Ceci est un Label" , bg = "#87CEEB") #cree une zone de text 
texte1.pack()

bouton1 = Button(cadre1, text = "Bouton") #cree un bouton
bouton1.pack()

entre1 = Entry(fenetre, text = "Rechercher") #cree une zone de recherche
entre1.pack()

check_bouton1 = Checkbutton(fenetre, text= "Choix 1") #cree un check bouton
check_bouton1.pack()

case_cocher1 = Radiobutton (fenetre, text = "choix 1") #cree un radio bouton
case_cocher1.pack()

liste = Listbox() #cree une liste d'option
liste.insert(1, "choix 1")
liste.insert(2, "choix 2")
liste.pack()

spin1 = Spinbox(fenetre) 
spin1.pack()

menu1 = Menu(fenetre)
menu1.add_cascade(label="Fichier")
menu1.add_cascade(label="Option")
menu1.add_cascade(label="Aide")
fenetre.config(menu = menu1)


fenetre.mainloop() #affichage de la fenetre


