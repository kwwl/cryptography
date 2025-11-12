import string


def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        crypted_text += chr((ord(char) + key) % 1_114_112)
    return crypted_text


def cesar_uncipher(crypted_message, key):
    return cesar_cipher(crypted_message, key)


def hack_cesar_cipher(crypted_message, alphabet):
    for possible_key in range(0, 1_114_112):
        possible_decryption == cesar_cipher(crypted_message, possible_key)
        if possible_decryption[à] in alphabet:
            print(possible_key)
            print(possible_devryption)
            print("_" * 20)


message = "chocolat"
crypted_message = cesar_cipher(message, 1000)
hack_cesar_cipher(crypted_message, alphabet=string.printable)
# initial_message =
