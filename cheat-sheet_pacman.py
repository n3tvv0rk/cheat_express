#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 


fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

#event = ''
touche = event.keysym
if touche == 'Return':
	print("hello")
	fenetre.destroy()

fenetre.mainloop()
