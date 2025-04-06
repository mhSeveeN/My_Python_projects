"""
    Program liczący Pole i Obwód podanej przez użytkownika figury na podstawie podanych przez użytkownika wartości.
    <Zastosowane funkcje: Kwadrat, Trojkat, main>
    <Autor: 05240405237>
"""

import string
import math

def Kwadrat():
    a=int(input("Podaj dlugosc boku a: "))
    Pole = a*a
    Obwod = 4 * a 
    
    print(f"Pole kwadratu wynosi: {Pole}, a obwód: {Obwod}.")
    
def Trojkat():
    a=int(input("Podaj długośc boku a: "))
    h=int(input("Podaj długość wysokości: "))
    Pole = (a * h) / 2
    Obwod = 3 * a
    
    print(f"Pole trojkata wynosi: {Pole}, a obwód: {Obwod}.")
    
def Prostokat():
    a=int(input("Podaj długośc boku a: "))
    b=int(input("Podaj długośc boku b: "))
    Pole = a * b
    Obwod = 2 * a + 2*b
    
    print(f"Pole prostokata wynosi: {Pole}, a obwód: {Obwod}.")
    
def Trapez():
    a=int(input("Podaj długośc boku a: "))
    b=int(input("Podaj długośc boku b: "))
    h=int(input("Podaj długość wysokości: "))
    c=int(input("Podaj długośc boku c: "))
    d=int(input("Podaj długośc boku d: "))
    Pole = 0.5 * (a + b) * h
    Obwod = a+b+c+d
    
    print(f"Pole trapezu wynosi: {Pole}, a obwód: {Obwod}.")
    
def main():
    print("Program liczący Pole i obwód wybranej figury. \n")
    choice = input("Twoja figura to (kwadrat/trojkat/prostokat/trapez): ").strip().lower()
    
    if choice == "kwadrat": {
        Kwadrat()
    } 
    elif choice == "trojkat": {
        Trojkat()
    }
    elif choice == "prostokat": {
        Prostokat()
    }
    elif choice == "trapez": {
        Trapez()
    }
    else: {
        print("Nieprawidlowa figura!")
    }
    
    
if __name__ == "__main__":
    main()