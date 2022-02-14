BRAILLE_CODE = { 'A':' 1',     'B':' 13',   'C':' 12',   'D':' 124',   'E':' 14',    'F':' 123',
                    
                 'G':' 1234',  'H':' 134',  'I':' 23',   'J':' 234',   'K':' 15',    'L':' 135',
                    
                 'M':' 125',   'N':' 1245', 'O':' 145',  'P':' 1235',  'Q':' 12345', 'R':' 1345',
                    
                 'S':' 235',   'T':' 2345', 'U':' 156',  'V':' 1356',  'W':' 2346',  'X':' 1256',
                    
                 'Y':' 12456', 'Z':' 1456', ' ':' '  }
  

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ':  
            cipher += BRAILLE_CODE[letter] + ''
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
