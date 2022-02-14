MORSE_CODE_DICT = { 'A':' .-',     'B':' -...',   'C':' -.-.',   'D':' -..',    'E':' .',      'F':' ..-.',
                    
                    'G':' --.',    'H':' ....',   'I':' ..',     'J':' .---',   'K':' -.-',    'L':' .-..',
                    
                    'M':' --',     'N':' -.',     'O':' ---',    'P':' .--.',   'Q':' --.-',   'R':' .-.',
                    
                    'S':' ...',    'T':' -',      'U':' ..-',    'V':' ...-',   'W':' .--',    'X':' -..-',
                    
                    'Y':' -.--',   'Z':' --..',   '1':' .----',  '2':' ..---',  '3':' ...--',  '4':' ....-',
                    
                    '5':' .....',  '6':' -....',  '7':' --...',  '8':' ---..',  '9':' ----.',  '0':' -----',
                    
                    ',':' --..--', '.':' .-.-.-', '?':' ..--..', '/':' -..-.',  '-':' -....-', '(':' -.--.',

                    ')':' -.--.-', ' ':' ' } 
  

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ':  
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:  
            cipher += ' '
    return cipher

def main():  
    message = input()
    result = encrypt(message)
    print(result)
    
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

if __name__ == '__main__':
    while True:
        main()
