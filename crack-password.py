import itertools
import string
import re 

def guess_password():    
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == userInput:
                return 'Password is {}. Found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)
            
            

userInput=input('Please enter password: ')  
symbol_collection = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

while (symbol_collection.search(userInput) != None): 
    print('Text has special characters, please do not use them.')
    userInput=input('Please enter password: ')   
    if(symbol_collection.search(userInput) == None): 
        print(guess_password()) 
 

