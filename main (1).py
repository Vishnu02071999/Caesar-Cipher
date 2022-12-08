import Encrypt
import Decrypt

Encrypt_Word = input(
  "Please enter the word that you want to encrypt: \n").lower(
  )
shift = int(input("Enter the shift for Encryption : "))
Encrypt.encryption(Encrypt_Word, shift)
Encrypted_Word = input("Enter the encrypted word: \n")
Decrypt.decryption(Encrypted_Word, shift)