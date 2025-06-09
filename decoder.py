MORSE_ROLES = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..',  '\'': '.----.',
    '!': '-.-.--', '/': '-..-.',   '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...',  ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-',  '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'  # slash - standard for separating words
}

class Decoder:
    def __init__(self):
        self.roles = MORSE_ROLES
        # Reversed morse dict key: value -> value: key for decoding
        self.reversed = {value: key for key, value in self.roles.items()}

    def encode(self, message):
        message = message.strip()

        try:
            return ' '.join([self.roles[s.upper()] for s in message])
        except KeyError as error:
            return f"Error, {error} is unknown Symbol."


    def decode(self, message):
        decode_message = []
        # Split for words
        words = message.strip().split('/')
        for word in words:
            # Split for letters
            letters = word.strip().split(' ')
            # Small errorchecking
            decode_message.append(''.join([self.reversed.get(l, f'<"{l}" is unknown Symbol>') for l in letters]))
        return ' '.join(decode_message).title()
