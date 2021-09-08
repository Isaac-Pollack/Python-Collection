"""
// Adder Problem //
Re-create the ADDER REPL making good use of string methods. // INCOMPLETE
"""

# easy way to handle dict addition

repl = {}
current_input = ''  # Define it as a string so we can immediately check for 'quit'

while 'quit' not in current_input:  # OUR CORE LOOP
    current_input = input('??? ').split()  # Input and split into a list of 2-3 values (action and var/val)

    # OUR SPECIFIC WORD FUNCTIONS, ALSO MODULAR IN PREP FOR Q2
    if 'input' in current_input and len(current_input) == 2:
        if current_input[1].isalpha():
            temp_var = current_input[1]
            temp_val = input('Enter a value for {}: '.format(current_input[1]))
            repl.update({'{}'.format(temp_var): temp_val})
        else:
            print('Syntax Error')
    elif 'input' in current_input and len(current_input) != 2:
        print('Syntax Error')

    if 'print' in current_input and len(current_input) == 2:
        if current_input[1].isalpha():
            temp_var = current_input[1]
            print('{}'.format(current_input[1]) + ' equals', (repl.get(current_input[1], 'This entry has no value set.')))
        else:
            print('Syntax Error')
    elif 'print' in current_input and len(current_input) != 2:
        print('Syntax Error')

    if 'gets' in current_input and len(current_input) == 3:
        if current_input[0].isalpha() and current_input[2].isalpha() or current_input[2].isdigit():  # If digit OR A-Z
            temp_var = current_input[0]
            temp_val = current_input[2]
            repl.update({'{}'.format(temp_var): temp_val})
        else:
            print('Syntax Error')
    elif 'gets' in current_input and len(current_input) != 3:
        print('Syntax Error')

    if 'adds' in current_input:
        if current_input[0].isalpha() and current_input[2].isalpha() or current_input[2].isdigit():  # If digit OR A-Z
            temp_var = repl['{}'.format(current_input[0])]
            temp_val = temp_var + repl['{}'.format(current_input[2])]
            repl.update({temp_var: temp_val})
        else:
            print('Syntax Error')
    elif 'adds' in current_input and len(current_input) != 3:
        print('Syntax Error')

    # FINAL error check for single entry that is not QUIT
    if len(current_input) == 1 and 'quit' not in current_input:
        print('Syntax Error')

else:
    print('Goodbye.')  # Exit the REPL.
