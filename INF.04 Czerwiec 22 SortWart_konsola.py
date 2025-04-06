"""
    Program wykorzystujący mechanizm przeszukiwania tablicy liczb pseudolosowych z wartownikiem.
    Autor: mhSeveeN
"""

import random

def Wartownik(array, search):
    array.append(search)
    
    i = 0
    while array[i] != search:
        i += 1
    if i<len(array)-1:
        return i
    else:
        return -1
    
def main():
    array=[random.randint(1,100) for _ in range(50)]
    search = int(input("Podaj liczbę do wyszukania: "))
    indeks = Wartownik(array, search)
    
    print(f"Przeszukiwana tablica to: {array}")
    
    if indeks != -1:
        print(f"Element {search} znaleziony na indeksie: {indeks}")
    else:
        print(f"Element {search} nie znajduje się w tablicy.")
        
if __name__ =="__main__":
    main()