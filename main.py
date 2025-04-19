from dekriptimiTekstit import decrypt_text
from enkriptimiTekstit import encrypt_text

key = b'0123456789abcdef' #Celesi universal qe do perdorim si shembull
while True:
    prgj = input("Deshironi te enkriptoni(e) apo dekriptoni(d)?\n")

    if(prgj == 'e'):
        plain_text = input("Shenoni mesazhin per ta enkriptuar: ")
        encrypted_text = encrypt_text(plain_text)
        print("Mesazhi juaj i enkriptuar eshte: " + encrypted_text)
        break;
    elif(prgj == 'd'):
        encrypted_text = input("Shenoni tekstin e enkriptuar: ")
        decrypted_text = decrypt_text(encrypted_text)
        print("Mesazhi i dekriptuar eshte: " + decrypted_text)
        break;
    else:
        print("Ju lutem jepni pergjigje valide (e ose d)\n")
