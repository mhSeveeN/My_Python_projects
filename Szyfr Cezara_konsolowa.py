"""
Program implementujący szyfr Cezara jak i szyfr przestawieniowy w konsoli oraz szyfrujący i deszyfrujący wiadomość podaną przez użytkownika.
Autor: mhSeveeN
"""
def szyfrCezara(napis, klucz):
    szyfrogram = ""
    for i in napis:
        litera = klucz + ord(i)
        if litera > ord('z'):
            litera -= 26
        elif litera < ord('a'):
            litera += 26
            
        szyfrogram += chr(litera)
    
    return szyfrogram

napis = input("Podaj swoją wiadomość od zaszyfrowania: ")
klucz = 3

szyfrogram = szyfrCezara(napis, klucz)
print(szyfrogram)

napis = szyfrCezara(szyfrogram, -klucz)
print("Twoja wiadomość po zdeszyfrowaniu:\n")
print(napis)