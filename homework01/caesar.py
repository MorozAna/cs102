def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for char in plaintext:
        if (ord(char) >= 65 and ord(char) <= 90) or
        (ord(char) >= 97 and ord(char) <= 122):
            if (ord(char) >= 88 and ord(char) <= 90) or
            (ord(char) >= 120 and ord(char) <= 122):
                ciphertext = ciphertext + chr(ord(char) - 23)
            else:
                ciphertext = ciphertext + chr(ord(char) + 3)
        else:
            ciphertext = ciphertext + char
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        if (ord(char) >= 65 and ord(char) <= 90) or
        (ord(char) >= 97 and ord(char) <= 122):
            if (ord(char) >= 65 and ord(char) <= 67) or
            (ord(char) >= 97 and ord(char) <= 99):
                plaintext = plaintext + chr(ord(char) + 23)
            else:
                plaintext = plaintext + chr(ord(char) - 3)
        else:
            plaintext = plaintext + char
    return plaintext
