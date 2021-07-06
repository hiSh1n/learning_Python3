#basic cisar cipher encryption and decryption in python.

#encryption
message = input('enter the message:')  
alphabet = 'abcdefghijklmnopqrstuvwxyz'
Key = 5
encrypt = ''
for i in message : 
    position = alphabet.find(i)
    newposition = (position + 5) % 26
    encrypt += alphabet[newposition]
print(encrypt)

#decryption
encrypt = input('enter the encrypt:')  
alphabet = 'abcdefghijklmnopqrstuvwxyz'
Key = 5
decrypt = ''
for i in encrypt : 
    Pposition = alphabet.find(i)
    newPposition = (Pposition - 5) % 26
    decrypt += alphabet[newPposition]
print(decrypt)
