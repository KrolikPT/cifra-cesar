##
## ===========================================
## =============== CIFRA CESAR ===============
## ===========================================
##
## Authors: 
##   Krolik

import os

letters = "abcdefghijklmnopqrstuvwxyz".upper()

def encrypt():
    try:
        pos = 0
        left = 0
        cipher_text = ""
        letters_key = int(input("CHAVE (ENTRE 1 E 25): "))
        
        if letters_key < 1 or letters_key > 25:   
            print("Valores apenas entre 1 e 25")
            exit()
            
        plain_text = input("TEXTO: ").upper()
        
        for c in plain_text:
            
            if c == " ":
                cipher_text += " "
                
            if c not in letters and c != " ":
                cipher_text += "?"
               
               
            for l in letters:
                if c == l:
                    pos = letters.index(c) + 1
                    
                    if pos + letters_key >= len(letters):
                        left = (pos + letters_key) - len(letters)
                        cipher_text += (letters[left - 1])
                    else:
                        cipher_text += (letters[pos + letters_key - 1])
                     
                        
        print("TEXTO ENCRIPTADO: %s" % (cipher_text))
        cipher_text = ""
            
    except Exception as e:
        print(e)
        
    
def decrypt():
    attempts = 25
    pos = 1
    decrypted_text = ""
    left = 0
    text_to_decrypt = input("TEXTO ENCRIPTADO: ").upper()

    while attempts > 0:
        for c in text_to_decrypt:
            
            if c == " ":
                decrypted_text += " "
            else:
                pos_letters = letters.index(c)
                        
                if (pos_letters + pos) >= len(letters):
                    left = (pos_letters + pos) - len(letters)
                    decrypted_text += letters[left]
                else:    
                    decrypted_text += letters[(pos_letters + pos)]
                                           
        print("\n-> %s <-" % (decrypted_text))
        decrypted_text = ""
        pos += 1    
        attempts -= 1
        

def main():
    print("################################################")
    print("################ CIFRA DE CESAR ################")
    print("################################################")
    print("# 1 - Encriptar")
    print("# 2 - Desencriptar")
    print("# 0 - Sair")
    option = input("# -> ")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if option == "1":
        encrypt()
    elif option == "2":
        decrypt()
    elif option == "0":
        exit()
    else:
        main()
            
            
if __name__ == "__main__":
    main()
