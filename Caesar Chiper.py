def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

def main():
    choice = input("Pilih operasi (enkripsi/dekripsi): ").strip().lower()
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan jumlah pergeseran (0-25): "))

    if choice == "enkripsi":
        result = caesar_encrypt(text, shift)
        print(f"Teks terenkripsi: {result}")
    elif choice == "dekripsi":
        result = caesar_decrypt(text, shift)
        print(f"Teks terdekripsi: {result}")
    else:
        print("Pilihan tidak valid. Silakan pilih 'enkripsi' atau 'dekripsi'.")

if __name__ == "__main__":
    main()
