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

        if veprimi == '1':
            plain_text = input("Shkruani tekstin për enkriptim:")
            encrypted = encrypt_text(plain_text)
            print(" Teksti i enkriptuar: "+encrypted)
        elif veprimi == '2':
            encrypted_text = input("Shkruani tekstin e enkriptuar: ")
            decrypted = decrypt_text(encrypted_text)
            print(" Teksti i dekriptuar: "+decrypted)
        else:
            print(" Zgjedhje e pavlefshme për tekst.")


    elif tipi == '2':
        print("\n Veprim për fajll: ")
        print("1. Enkripto")
        print("2. Dekripto")

        veprimi = input("Zgjedhja juaj: ")

        if veprimi == '1':
            enkripto()
        elif veprimi == '2':
            dekripto()
        else:
            print(" Zgjedhje e pavlefshme për fajll.")


    elif tipi == '3':
        print(" Dalje nga programi.")
        break
    else:
        print("Ju lutem zgjidhni 1, 2 ose 3.\n")
        
        if veprimi == '1':
            plain_text = input("Shkruani tekstin për enkriptim: ")
            encrypted = encrypt_text(plain_text)
            print(" Teksti i enkriptuar: " + encrypted)
