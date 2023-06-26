# Converts text to morse code. Currently only 1 direction

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
    user_input = input('What would you like to translate? (Exit to close program) ')  # message to translate
    output = str('')  # define output and reset var
    if user_input.upper() != 'EXIT':
        try:
            # check each char against dictionary to translate
            for char in user_input.upper():
                morse_equiv = morse_code_dict[char]
                output = output + morse_equiv + ' '
            print(f'Translated Message is: {output}')
            repeat = input('Would you like to translate another message? (Y/N)')
            if repeat.upper() == 'N' or repeat.upper() == 'NO':
                break
            else:
                continue
        except KeyError:
            print("A character couldn't be translated. Only standard English characters"
                  " are supported at this time, please try again.")
        except:
            print("Something went wrong! Please check your message and try again.")
    else:
        break


