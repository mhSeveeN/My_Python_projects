import math

def NWD(liczba1, liczba2):
    while liczba2!=0:
        liczba1, liczba2 = liczba2, liczba1 % liczba2
        return liczba1
    

def Euklides():
    print("Program stosujący algorytm Euklidesa na liczbach calkowitych podanych przez użytkownika.")
    try:
        liczba1 = int(input("Podaj pierwszą liczbę: "))
        liczba2 = int(input("Podaj drugą liczbę: "))
        wynik = NWD(liczba1, liczba2)
        print(f"NWD z liczby {liczba1} i {liczba2} wynosi: {wynik}")
    except ValueError:
        print("Podaj liczbę całkowitą!!")
        
def main():
    Euklides()
    
if __name__=="__main__":
    main()