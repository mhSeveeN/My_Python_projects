""" 
    /********************************************************
    * nazwa funkcji:       <SortowanieprzezWybor>
    * parametry wejściowe: <array> - <zawartość tablicy>
    <user_input> - <wartości wprowadzane przez użytkownika>
    <i, j, min index> - <dane i zachowanie tablicy>
    * wartość zwracana:    <co zwraca funkcja – opis> 
    * autor:               <05240405237> 
    * ****************************************************/ 
"""
def SortowanieprzezWybor (array):
    n = len(array)
    for i in range (n-1):
        min_index = i
        for j in range(i +1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]

def main():
    print("Program służący do sortowania przez wybór tablicy 10 liczb całkowitych podanych przez użytkownika.")
    print("Wprowadź 10 liczb całkowitych:")
    user_input=[]
    for i in range(10):
        while True:
            try:
                number = int(input(f"Liczba {i + 1}: "))
                user_input.append(number)
                break
            except ValueError:
                print("Podaj poprawną liczbę całkowitą.")
    
    print(f"Zawartość tablicy podana przez użytkownika: {user_input}")

    SortowanieprzezWybor(user_input)
    
    print("Posortowana tablica:")
    print(user_input)
    

if __name__=="__main__":
    main()