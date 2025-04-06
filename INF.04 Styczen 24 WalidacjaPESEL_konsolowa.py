"""
    Program sprawdzający płeć na podstawie nr pesel oraz sprawdzajacy sumę kontrolną.
    Pesel wprowadza użytkownik
    Autor: mhSeveeN
"""
def PeselValidate(pesel):
    if len(pesel) !=11:
        return False
    
    suma_kontrolna = int(pesel[10])
    plec = int(pesel[10])
    
    if (plec %2 == 0):
        print(f"PESEL {pesel} należy do Kobiety.")
    else:
        print(f"PESEL {pesel} należy do mężczyzny.")
    
    wagi = [1,3,7,9,1,3,7,9,1,3,1]
    Liczona_suma_kontolna = sum(int(cyfra) * waga for cyfra, waga in zip(pesel[:10], wagi)) % 10
    if Liczona_suma_kontolna !=0:
        Liczona_suma_kontolna = 10-Liczona_suma_kontolna
    return Liczona_suma_kontolna == suma_kontrolna



if __name__ == "__main__":
    pesel = str(input("Podaj swoj nr PESEL: "))
    if PeselValidate(pesel):
        print(f"PESEL {pesel} jest poprawny")
    else:
        print(f"PESEL {pesel} nie jest poprawny")