"""
    Aplikacja desktopowa implementujaca założenia generowania hasła dla pracowników.
    Arkusz INF04 Styczeń 2023
    Python
    Autor: mhSeveeN
"""
import tkinter as tk
from tkinter import messagebox
import string
import random

def Generowanie_hasla():
    try:
        lenght = int(hasloDL_entry.get())
        if lenght <=0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną liczbę znaków większą od zera.")
        return
    
    characters = string.ascii_lowercase
    if letters_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if specials_var.get():
        characters += "!@#$%^&*()_-+="
        
    if not characters:
        messagebox.showerror("Błąd", "Wybierz co najmniej jedną opcję generowania hasła")
        return
    
    haslo = ''.join(random.choice(characters) for _ in range(lenght))
    if letters_var.get():
        haslo = random.choice(string.ascii_uppercase) + haslo[1:]
    if digits_var.get():
        haslo = random.choice(string.digits) + haslo[1:]
    if specials_var.get():
        haslo = random.choice("!@#$%^&*()_-+=") + haslo[1:]
    
    haslo_entry.delete(0, tk.END)
    haslo_entry.insert(0, haslo)
    
def potwierdz_dane():
    name = name_entry.get()
    surname = surname_entry.get()
    pozycja = pozycja_var.get()
    haslo = haslo_entry.get()
    
    if not name or not surname or not pozycja or not haslo:
        messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione")
        return
    
    messagebox.showinfo("Dane pracownika", f"Dane pracownika: {name} {surname} {pozycja} {haslo}")
    
    
okno = tk.Tk()
okno.title("Dodaj pracownika")
okno.configure(bg="#B0C4DE")

frame_employee = tk.LabelFrame(okno, text="Dane pracownika", bg="#B0C4DE", font=("Arial", 10))
frame_employee.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

tk.Label(frame_employee, text="Imię:", bg="#B0C4DE").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame_employee)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_employee, text="Nazwisko:", bg="#B0C4DE").grid(row=1, column=0, padx=5, pady=5, sticky="e")
surname_entry = tk.Entry(frame_employee)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_employee, text="Stanowisko:", bg="#B0C4DE").grid(row=2, column=0, padx=5, pady=5, sticky="e")
pozycja_var = tk.StringVar(value="")
pozycja_menu = tk.OptionMenu(frame_employee, pozycja_var, "Kierownik", "Starszy programista", "Młodszy programista", "Tester")
pozycja_menu.grid(row=2, column=1, padx=5, pady=5)

frame_haslo = tk.LabelFrame(okno, text="Generowanie hasła", bg="#B0C4DE", font=("Arial", 10))
frame_haslo.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(frame_haslo, text="Liczba Znaków?", bg="#B0C4DE").grid(row=0, column=0, padx=5, pady=5, sticky="e")
hasloDL_entry = tk.Entry(frame_haslo)
hasloDL_entry.grid(row=0, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=False)
specials_var = tk.BooleanVar(value=False)

letters_check = tk.Checkbutton(frame_haslo, text="Małe i wielkie litery", variable=letters_var, bg="#B0C4DE")
letters_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

digits_check = tk.Checkbutton(frame_haslo, text="Cyfry", variable=digits_var, bg="#B0C4DE")
digits_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

specials_check = tk.Checkbutton(frame_haslo, text="Znaki specjalne", variable=specials_var, bg="#B0C4DE")
specials_check.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

haslo_entry = tk.Entry(frame_haslo)
haslo_entry.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

generuj_przycisk = tk.Button(frame_haslo, text="Generuj hasło", command=Generowanie_hasla, bg="#4682B4", fg="white")
generuj_przycisk.grid(row=5, column=0, columnspan=2, pady=10)

potwierdz_przycisk = tk.Button(okno, text="Zatwierdź", command=potwierdz_dane, bg="#4682B4", fg="white", width=20)
potwierdz_przycisk.grid(row=1, column=0, columnspan=2, pady=10)

okno.mainloop()
