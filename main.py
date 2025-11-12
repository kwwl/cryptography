def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        crypted_text += chr((ord(char) + key) % 1_114_112)
    return crypted_text

def cesar_uncipher(crypted_message, key):
    return cesar_cipher(crypted_message, key)

initial_message = 
crypted_message = cesar_cipher("chocolat", 1000)
print(crypted_message)
