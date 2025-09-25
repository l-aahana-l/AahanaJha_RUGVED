def caesarCipher(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted.append(chr(shifted))
        else:
            encrypted.append(char)
    return ''.join(encrypted)
text=input("Enter the text:")
shift=int(input("Enter the shift:"))
print(caesarCipher(text,shift))
