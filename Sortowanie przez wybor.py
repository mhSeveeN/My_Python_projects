def SortPWybor(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
if __name__ == "__main__":
    lista = int(input("Podaj 5 liczb: "))
    print("Przed sortowaniem: ", lista)
    SortPWybor(lista)
    print("Po przesortowaniu: ", lista)