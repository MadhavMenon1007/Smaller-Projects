def caesar_shift(phrase, key):
    list_of_chars = [i for i in phrase]
    encrypted_list = []
    encrypted_message = ""
    for i in list_of_chars:
        if i == " ":
            list_of_chars.remove(i)
        encrypted_list.append(chr(ord(i)+key))
    return encrypted_message.join(encrypted_list)
    

def decode_caesar_shift(cipher_text, key):
    list_of_chars = [i for i in cipher_text]
    decrypted_list = []
    decrypted_message = ""
    for i in list_of_chars:
        if i == " ":
            list_of_chars.remove(i)
        decrypted_list.append(chr(ord(i)-key))
    return decrypted_message.join(decrypted_list)

