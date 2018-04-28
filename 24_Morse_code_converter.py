def encode(text):
    CODE = {'a': '.-',     'b': '-...',   'c': '-.-.', 
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
     	's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
    morse = ""
    words = text.lower().split()
    for word in words:
        for letter in word:
            morse += CODE[letter]
            morse += "/"
        morse += "/"
    morse += "/"
    return morse

print(encode("abc"))  # .-/-.../-.-.///
print(encode("susenka"))  # .../..-/..././-./-.-/.-///
print(encode("xy z")) # -..-/-.--//--..///
print(encode("SOS"))
print(encode("SoloLearn"))
