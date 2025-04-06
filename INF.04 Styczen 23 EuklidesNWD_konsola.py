"""
    Program wykorzystujący mechanikę algorytmu Euklidesa dla liczb całkowitych dodatnich
    Autor: mhSeveeN
"""
import math

def NWD(number_1, number_2):
    while number_2 !=0:
        number_1, number_2 = number_2, number_1 % number_2
        return number_1
    
def Euklides():
    print("Program stosujący Algorytm Euklidesa dla liczb całkowitych dodatnich.")
    try:
        number_1 = int(input("Podaj pierwszą liczbę całkowitą dodatnią: "))
        number_2 = int(input("Podaj drugą liczbę całkowitą dodatnią: "))
        wynik = NWD(number_1, number_2)
        print(f"NWD z liczby {number_1} i {number_2} wynosi: {wynik}.")
    except ValueError:
        print("Podaj liczbę całkowitą dodatnią!!")
        
def main():
    Euklides()
        
if __name__=="__main__":
    main()