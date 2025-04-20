from enkriptimiTekstit import encrypt_text
from dekriptimiTekstit import decrypt_text
from EnkriptimiiFileve import enkripto
from DekriptimiiFileve import dekripto

while True:
    print("\n Zgjidh llojin e të dhënave:")
    print("1. Tekst")
    print("2. Fajll")
    print("3. Dil")

    tipi = input("Zgjedhja juaj: ")

    if tipi == '1':
        print("\n Veprim për tekst:")
        print("1. Enkripto")
        print("2. Dekripto")

        veprimi = input("Zgjedhja juaj: ")



    elif tipi == '2':
        print("\n Veprim për fajll:")
        print("1. Enkripto")
        print("2. Dekripto")

        veprimi = input("Zgjedhja juaj: ")



    elif tipi == '3':
        print(" Dalje nga programi.")
        break
    else:
        print("Ju lutem zgjidhni 1, 2 ose 3.")
