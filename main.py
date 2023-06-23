# Converts text to morse code

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

while True:
    user_input = input('What would you like to translate? (Exit to close program) ')
    output = str('')
    if user_input.upper() != 'EXIT':
        for char in user_input.upper():
            morse_equiv = morse_code_dict[char]
            output = output + morse_equiv + ' '
        print(f'Translated Message is: {output}')
        repeat = input('Would you like to translate another message? (Y/N)')
        if repeat.upper() == 'Y' or repeat.upper() == 'YES':
            continue
        elif repeat.upper() == 'N' or repeat.upper() == 'NO':
            break
        else:
            repeat = input('Would you like to translate another message? (Y/N)')
    else:
        break


