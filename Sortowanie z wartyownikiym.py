"""
******************************************************
nazwa funkcji: <wartoiwnik, main>
argumenty: <tablica> - <liczby pseudolosowe z przedzialu 0 do 100>, <szukana> - <szukana wartosc> 
typ zwracany: <indeks>, <miejsce z tablicy>
informacje: <opis>
autor: <05240405237> 
***************************************************** 
"""
import random

def wartownik(tablica, szukana):
    tablica.append(szukana)
    
    i = 0
    while tablica[i] != szukana:
        i += 1
    if i< len(tablica) - 1:
        return i
    else:
        return -1

        
def main():
    tablica = [random.randint(0, 100) for _ in range(100)]

    szukana = int(input("Podaj liczbę do wyszukania: "))
    
    indeks = wartownik(tablica, szukana)
    
    if indeks != -1:
        print(f"Element {szukana} znaleziony na indeksie {indeks}.")
    else: 
        print(f"Element {szukana} nie znajduje sie w tablicy.")
    
if __name__ == "__main__":
    main()