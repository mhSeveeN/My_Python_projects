"""
    Program wykorzystujący implementację mechanizmu sortowania poprzez wybór
    Autor: mhSeveeN
"""
def SortowaniePrzezWybor(tablica):
    n = len(tablica)
    for i in range (n-1):
        minimal_index = i
        for j in range (i+1, n):
            if tablica[j] < tablica[minimal_index]:
                minimal_index = j
                
        tablica[i], tablica[minimal_index] = tablica[minimal_index], tablica[i]
        

def main():
    print("Program wykorzystujący mechanizm sortowania przez wybór.")
    print("Wprowadź 10 liczb całkowitych")
    liczby=[]
    for i in range(10):
        while True:
            try:
                number = int(input(f"Liczba {i+1}: "))
                liczby.append(number)
                break
            except ValueError:
                print("Podaj porawną liczbę całkowitą!!")
    
    print(f"Zawartośc tablicy podana przez użytkownika: {liczby}")
    
    SortowaniePrzezWybor(liczby)
    
    print("Posortowana tablica:")
    print(liczby)
    
if __name__=="__main__":
    main()