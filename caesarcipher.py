# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 13:40:20 2025

@author: dcriggjp
"""

LOWERCASE_RANGE = range(ord('a'), ord('z') + 1)
UPPERCASE_RANGE = range(ord('A'), ord('Z') + 1)

def get_encrypt_decript(message: str='Do you you want to (e)ncrypt or (d)ecrypt?\n> ') -> str:
    mode = input(message)
    
    if mode not in ['e', 'd']:
        raise ValueError(f'`{mode}` is not a valid parameter. Valid parameters are `e` and `d`.')
    return mode
    

def get_key(message: str='Please enter the key (0 to 25) to use.\n> ') -> int:
    key = input(message)
    try: 
        key = int(key)
    except:
        raise ValueError(f'{key} cannot be converted to integer')
    if not 0 <= key <= 25:
        raise ValueError(f'{key} must be between 0 and 25, inclusive.')
    return key


def get_message_to_encrypt_decrypt(message: str) -> str:
    message_to_encrypt = input(message)
    for char in message_to_encrypt:
        if (not char.isalpha()) and (not char.isspace()):
            raise ValueError(f'`{char} is not a letter.`')
    return message_to_encrypt


def apply_cipher_to_char(char: str, key: int) -> str:
    new_ord = ord(char) + key
    if not chr(new_ord).isalpha():
        new_ord += 26 # Wrap around by length of alphabet
    new_char = chr(new_ord)
    return new_char


def unapply_cipher_to_char(char: str, key: int) -> str:
    new_ord = ord(char) - key
    if not chr(new_ord).isalpha():
        new_ord -= 26 # Wrap around by length of alphabet
    new_char = chr(new_ord)
    return new_char


def apply_cipher_to_message(message: str, key: int) -> str:
    encrypted_message = ''
    for m in message:
        if m.isspace():
            encrypted_message += m
        else:
            encrypted_message += apply_cipher_to_char(m, key)
    return encrypted_message


def unapply_cipher_to_message(message: str, key: int) -> str:
    encrypted_message = ''
    for m in message:
        if m.isspace():
            encrypted_message += m
        else:
            encrypted_message += unapply_cipher_to_char(m, key)
    return encrypted_message
    

def encrypt_message():
        message_to_encrypt = get_message_to_encrypt_decrypt('Enter the message to encrypt:\n> ')
        key = get_key()
        encrypted_message = apply_cipher_to_message(message_to_encrypt, key)
        print(f'Encrypted message: {encrypted_message}.')
        
        
def decrpyt_message():
        message_to_decrypt = get_message_to_encrypt_decrypt('Enter the message to decrypt:\n> ')
        key = get_key()
        decrypted_message = unapply_cipher_to_message(message_to_decrypt, key)
        print(f'Decrypted message: {decrypted_message}.')


if __name__ == '__main__':
    mode = get_encrypt_decript()
    if mode == 'e':
        encrypt_message()
    elif mode == 'd':
        decrpyt_message()
        
        
        
        
        