'''Simple calculator, takes two integer numbers and an operator (+, -, *, /) as inputs
    and prints out result of the selected operation'''


import operator, string

operations = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
error_msg = "Oops! I don't recognize that. Try again..."


while True:
    number1 = (input('Enter a number (or a single letter to exit): '))
    try:
        number1 = int(number1)

        while True:
            operator = input('Enter an operator (+ - * or /): ')
            if operator in operations.keys():
                break
            else:
                print(error_msg)

        while True:
            try:
                number2 = int((input('Enter another number: ')))
                break
            except ValueError:
                print(error_msg)
                
        print('Result: ' + str(operations[operator](number1, number2)))
        
    except ValueError:
        if len(number1) == 1 and number1 in string.ascii_letters:
            break
        else:
            print(error_msg)
    
  


    
    
    
    
    













#        print("Oops!  That is not a valid number.  Try again...")
#
#        print("Oops!  That is not a valid operation.  Try again...")





