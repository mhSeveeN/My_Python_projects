import tkinter as tk
from tkinter import *

okno = tk.Tk()
okno.title("Notatnik")
okno.geometry("450x250")

label = tk.Label(okno, text="Tworzenie Notatek")
for i in range(1,2):
    notatki = []
    notatka = input("Napisz coś:")
    notatki.append(notatka)
label.pack()
button = tk.Button(okno, text="Wyswietl notatke!", command=lambda:print(f"Notatka {i}: {notatki[0]}"))
button. pack()

okno.mainloop()