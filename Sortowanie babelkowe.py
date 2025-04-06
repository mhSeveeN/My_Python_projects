import random

def generuj_tablice(rozmiar):
    return [random.randint(0,100) for _ in range(rozmiar)]

def bubble_sort(tablica):
    n = len(tablica)
    for i in range(n):
        zamienione = False
        for j in range(0, n-i-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
                zamienione = True
        if not zamienione:
            break
    return tablica

rozmiar_tablicy = 10

tablica = generuj_tablice(rozmiar_tablicy)
print("Tablica przed posortowaniem: ", tablica)
tablica_posortowana = bubble_sort(tablica)
print("Tablica po posortowaniu: ", tablica_posortowana)