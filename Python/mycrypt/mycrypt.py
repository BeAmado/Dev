#!/usr/bin/env python3
def mongCipher(s, offset):
    offset %= 10
    crypt = ''
    for c in s:
        crypt += str((int(c) + offset) % 10)

    return crypt

def cryptStr(s):
    crypted = ''
    for i in range(len(s)):
        if (i != 8):
            crypted += mongCipher(s[i], i)
        else:
            crypted += s[i]

    return crypted

def decryptStr(s):
    decrypted = ''
    for i in range(len(s)):
        if (i != 8):
            decrypted += mongCipher(s[i], 10 - (i % 10))
        else:
            decrypted += s[i]

    return decrypted

def confirm(val):
    resp = raw_input('You chose "' + str(val) + '". Do you confirm your choice? (y/N)')
    if (resp.lower() in ['y', 'yes']):
        return True
    return False

def showOptions(op):
    print("Options:")
    for key in op.keys():
        print(str(key) + ' -> ' + str(op[key]))

def getUserOption():
    options = {1: 'encrypt', 2: 'decrypt'}
    userOp = None

    while True:
        showOptions(options)
        userOp = int(input('Enter the desired option: '))
        if (userOp in options.keys()):
            break
        else:
            print('Invalid option!')

    return options[userOp]
    

def main():
    print("\n------ CPF encryption/decryption program ----------\n\n")

    mode = getUserOption()

    if (mode == 'encrypt'):
        cpf = input('Enter the CPF to be encrypted: ')
        print("\nThe encrypted CPF is " + cryptStr(cpf) + "\n")
    elif (mode == 'decrypt'):
        cryptedCpf = input('Enter the encrypted CPF: ')
        print("\nThe decrypted CPF is " + decryptStr(cryptedCpf) + "\n")
    
    print("\n------------ END OF PROGRAM -----------\n")

main()
