def brute_force_caesar_cipher(s):
    for shift in range(26):
        decoded = ""

        for char in s:
            if 'a' <= char <= 'z':
                decoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                decoded += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                decoded += char

        print(f"Shift {shift}: {decoded}")

cipher_text = "Ugew gnwj zwjw Oslkgf"
brute_force_caesar_cipher(cipher_text)
