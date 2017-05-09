#!/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *

# Création de la fenêtre principale
Window = Tk()
background_color = '#3A3E3D'
Window.configure(bg=background_color)
Window.title('Pacman Notes')

def Clavier(event):
	""" Gestion de l'événement Appui sur une touche du clavier """
	touche = event.keysym
	#fermeture de fenêtre
	if touche == 'Return':
		Window.destroy()

pacman_file = 'documents/cheat_sheet/pacman.txt'
with open(pacman_file, 'r') as file:
	pacman_notes = file.read()

#l = LabelFrame(Window, text="Configuration", padx=20, pady=20)
#l.pack(fill="both", expand="no")
#Label(l, text=pacman_notes).pack()

#p = PanedWindow(Window, orient=HORIZONTAL)
#p.pack(side=TOP, expand=N, fill=BOTH, pady=2, padx=2)
#p.add(Label(p, text=pacman_notes, background='#3A3E3D', anchor=NW))
#p.add(Label(p, text='Volet 2', background='#3A3E3D', anchor=CENTER) )
#p.add(Label(p, text='Volet 3', background='#3A3E3D', anchor=CENTER) )
#p.pack()

canvas = Canvas(Window, width=500, height=700, background='#222222')
texte1 = canvas.create_text(235, 90, text=pacman_notes, font="Arial 9", fill="grey")
canvas.pack()


Window.focus_set()
Window.bind("<Key>", Clavier)
# Création d'un widget Button (bouton Quitter)
Button(Window, text ='Quitter', command = Window.destroy, relief=RAISED, cursor="pirate").pack(side=LEFT,padx=5,pady=5)

Window.mainloop()
