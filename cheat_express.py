#!/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

import os
import glob

# Create the choice window
dossier = os.path.dirname(os.path.abspath(__file__))+'/cheat_sheet/*.txt'
cheat = glob.glob(dossier)
element_selected = cheat[0]


def choice():
	Window = Tk()
	List = ttk.Combobox(Window)
	List.place(x=50,y=100)
	List['value'] = cheat
	List.current(0)

	def selection(event):
		global element_selected
		element_selected = List.get()

	def keyboard(event):
		key = event.keysym
		if key == 'Return':
			print('Return')
			Window.destroy()

	Window.focus_set()
	Window.bind('<<ComboboxSelected>>', selection)
	Window.bind('<Key>', keyboard)
	Window.mainloop()
	return element_selected

def display_sheet():
	Window2 = Tk()
	background_color = '#3A3E3D'
	Window2.configure(bg=background_color)
	Window2.title("Cheat Express")
	canvas = Canvas(Window2, width=500, height=700, background='#222222')
	with open(element_selected, "r") as blobi:
		content_blobi = blobi.read()
	texte1 = canvas.create_text(235, 90, text=content_blobi, font='Arial 9', fill='grey')
	canvas.pack()

	def keyboard(event):
		key = event.keysym
		if key == 'Return':
			Window2.destroy()

	Window2.focus_set()
	Window2.bind('<Key>', keyboard)
	# Create a button widget (button cancel)
	Button(Window2, text ='Cancel', command = Window2.destroy, relief=RAISED, cursor='pirate').pack(side=LEFT,padx=5,pady=5)
	Window2.mainloop()

choice()
display_sheet()
