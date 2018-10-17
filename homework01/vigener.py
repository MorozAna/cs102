def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ""
    i = 0
    for char in plaintext:
        if "a" <= char <= "z" or "A" <= char <= "Z":
            shift = ord(keyword[i])
            if "a" <= char <= "z":
                shift -= ord("a")
                if shift <= ord("z") - ord(char):
                    ciphertext += chr(ord(char) + shift)
                else:
                    ciphertext += chr(ord(char) - 26 + shift)
            else:
                shift -= ord("A")
                if shift <= ord("Z") - ord(char):
                    ciphertext += chr(ord(char) + shift)
                else:
                    ciphertext += chr(ord(char) - 26 + shift)
        else:
            ciphertext += char
        if len(keyword) == i + 1:
            i = 0
        else:
            i += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    plaintext = ""
    i = 0
    for char in ciphertext:
        if "a" <= char <= "z" or "A" <= char <= "Z":
            shift = ord(keyword[i])
            if "a" <= char <= "z":
                shift -= ord("a")
                if shift <= ord(char) - ord("a"):
                    plaintext += chr(ord(char) - shift)
                else:
                    plaintext += chr(ord(char) + 26 - shift)
            else:
                shift -= ord("A")
                if shift <= ord(char) - ord("A"):
                    plaintext += chr(ord(char) - shift)
                else:
                    plaintext += chr(ord(char) + 26 - shift)
        else:
            plaintext += char
        if len(keyword) == i + 1:
            i = 0
        else:
            i += 1
    return plaintext
