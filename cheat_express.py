#!/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *

# Create the main window
Window = Tk()
background_color = '#3A3E3D'
Window.configure(bg=background_color)
Window.title('Pacman Notes')

def Keyboard(event):
	""" Manage the event: Pressing a key on the keyboard """
	touche = event.keysym
	#close thewindow
	if touche == 'Return':
		Window.destroy()

pacman_file = '/home/n3tvv0rk/documents/cheat_sheet/pacman.txt'
with open(pacman_file, 'r') as file:
	pacman_notes = file.read()

canvas = Canvas(Window, width=500, height=700, background='#222222')
texte1 = canvas.create_text(235, 90, text=pacman_notes, font="Arial 9", fill="grey")
canvas.pack()


Window.focus_set()
Window.bind("<Key>", Keyboard)
# Create a button widget (button cancel)
Button(Window, text ='Cancel', command = Window.destroy, relief=RAISED, cursor="pirate").pack(side=LEFT,padx=5,pady=5)

Window.mainloop()
