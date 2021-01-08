def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    length = len(encrypted_text)
    plain_text = encrypted_text
    for i in range(n):
        decrypted_text = ""
        for j in range(int(length / 2)):
            decrypted_text += plain_text[i + int(length / 2)]
            decrypted_text += plain_text[i]
        if length % 2:
            decrypted_text += plain_text[-1]
        plain_text = decrypted_text
    return decrypted_text


def encrypt(text, n):
    if n < 1:
        return text
    plain_text = text
    for i in range(n):
        encrypted_text = ""
        for j in range(1, len(plain_text), 2):
            encrypted_text += plain_text[i]
        for j in range(0, len(plain_text), 2):
            encrypted_text += plain_text[i]
        plain_text = encrypted_text
    return encrypted_text
