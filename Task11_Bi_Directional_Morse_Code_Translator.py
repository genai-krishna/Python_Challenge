# =========================================================
# Bi-Directional Morse Code Translator
# Author: Krishna
# Description:
#   This program can:
#     1️⃣ Convert normal text into Morse code
#     2️⃣ Convert Morse code back into readable English text
# Concepts used: Dictionaries, Functions, Loops, String Handling
# =========================================================

# Morse Code Dictionary for Letters, Numbers, and Special Characters
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '!': '-.-.--', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', "'": '.----.'
}

# Reverse dictionary for decoding Morse → Text
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


# ---------------------------------------------------------
# Function: Encode text to Morse code
# ---------------------------------------------------------
def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char == " ":
            morse_code += " / "  # Use / for space between words
        elif char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += ""  # Ignore unsupported characters
    return morse_code.strip()


# ---------------------------------------------------------
# Function: Decode Morse code to Text
# ---------------------------------------------------------
def morse_to_text(morse):
    words = morse.split(" / ")  # Split Morse by word
    decoded_text = ""

    for word in words:
        letters = word.split()
        for letter in letters:
            decoded_text += REVERSE_MORSE_DICT.get(letter, "")
        decoded_text += " "
    return decoded_text.strip()


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
def main():
    print("===== Morse Code Translator =====")
    print("1. Text to Morse")
    print("2. Morse to Text")
    print("=================================")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        text = input("Enter text to convert: ")
        result = text_to_morse(text)
        print("\nMorse Code:")
        print(result)
        print("-" * 72)

    elif choice == "2":
        morse = input("Enter Morse code: ")
        result = morse_to_text(morse)
        print("\nDecoded Text:")
        print(result)
        print("-" * 72)

    else:
        print("Invalid choice! Please enter 1 or 2.")


# Run the program
if __name__ == "__main__":
    main()
