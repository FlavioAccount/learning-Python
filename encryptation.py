#This program will encrypt one password

import random
import string

def decrypt(encrip_pswrd, key, chars):
    password = " "
    for letter in encrip_pswrd:
        index = key.index(letter)
        password += chars[index]

    return password[2:] #Retira duas strings do password. Del algum BUG

def encrypt(password):
    chars = " " + string.punctuation + string.digits + string.ascii_letters #These strings are different string constants imported
    chars = list(chars) #It transforms the big string into a list

    key = chars.copy()#This method copies everything inside chars to key
    random.shuffle(key) #This method shuffles the list keye

    #Everytime this program is runned, the password will be encrypted using another characters
    #ENCRYPT
    encrip_pswrd = " "
    for letter in password:
        index = chars.index(letter)
        encrip_pswrd += key[index]

    print(f"original message: {password}")
    print(f"encripted message: {encrip_pswrd}")
    return encrip_pswrd, key, chars

def main():
    password = input("Enter your password here: ")
    pass_dcrp, key, chars = encrypt(password)
    decr_pass = decrypt(pass_dcrp, key, chars)
    print(f"Este e o password decriptado: {decr_pass}")

if __name__ == '__main__':
    main()