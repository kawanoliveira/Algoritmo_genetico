from CTkScrollableDropdown import *
from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.geometry("400x300")

# Some option list
values = ["individuo 1","individuo 1","individuo 1","individuo 1","individuo 1","individuo 1","individuo 1",]

# Attach to OptionMenu 
optionmenu = customtkinter.CTkOptionMenu(root, width=135, )
optionmenu.place(relx=0.5, rely=0.5, anchor=CENTER)

CTkScrollableDropdown(optionmenu, values=values, width=135, height=120)

root.mainloop()