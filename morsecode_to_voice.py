import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

MORSE_CODE_DICT = { 'A':' .-',     'B':' -...',   'C':' -.-.',   'D':' -..',    'E':' .',      'F':' ..-.',
                    
                    'G':' --.',    'H':' ....',   'I':' ..',     'J':' .---',   'K':' -.-',    'L':' .-..',
                    
                    'M':' --',     'N':' -.',     'O':' ---',    'P':' .--.',   'Q':' --.-',   'R':' .-.',
                    
                    'S':' ...',    'T':' -',      'U':' ..-',    'V':' ...-',   'W':' .--',    'X':' -..-',
                    
                    'Y':' -.--',   'Z':' --..',   '1':' .----',  '2':' ..---',  '3':' ...--',  '4':' ....-',
                    
                    '5':' .....',  '6':' -....',  '7':' --...',  '8':' ---..',  '9':' ----.',  '0':' -----',
                    
                    ',':' --..--', '.':' .-.-.-', '?':' ..--..', '/':' -..-.',  '-':' -....-', '(':' -.--.',

                    ')':' -.--.-', ' ':' ' } 
  
def decrypt(message): 
    message += ' '
    decipher = ' ' 
    citext = ' ' 
    for letter in message:  
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = ' ' 
    return decipher

def main():  
    message = input()
    result = decrypt(message)
    print(result)
    speak(result)
    
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

if __name__ == '__main__':
    while True:
        main()
