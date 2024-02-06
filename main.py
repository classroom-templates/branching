######################
# 
# Your comment header here
# 
######################

# Consants. Use these in your formulas
FREEZING_F = 32.0        # freezing point of water in Fahrenheit
MULTIPLIER_F = .5555556  # this is 5/9
MULTIPLIER_C = 1.8       # this is 9/5

# this function will be used below to determine
# if something is valid integer or float you do not
# need to understand it to use it, but read it and
# see if you can understand how it works.
def is_number(string):
    number = False
    if string.startswith('-'):
        string = string[1:]  # Remove the minus sign if it's at the beginning
    if string.count('.') == 1: # if there is a decimal point, it's a float
        # break it apart and check both sides for being all digits
        integer_part, decimal_part = string.split('.')
        if integer_part.isdigit() and decimal_part.isdigit():
            number = True
    elif string.isdigit(): # if it wasn't a float, it's an integer, so check it
        number = True

    return number

# this defines fahrenheit_to_celsius, but it does not run it
def fahrenheit_to_celsius(f):
    # STEP 1a: put your previous solution back in place here
    # see if you can reduce it to one line of code instead of 2    
    c = 0
    return c

# this defines celsius_to_fahrenheit, but it does not run it
def celsius_to_fahrenheit(c):
    # STEP 1b: put your previous solution back in place here
    # see if you can reduce it to one line of code instead of 2
    f = 0
    return f

# this defines main, but it does not run it
def main():
    #ask the user for a choice, 1, 2
    choice = input("Enter\n  1 C to F\n  2 F to C\n")

    if choice == "1":
        # choice is 1, ask for and convert celsius_to_fahrenheit
        celsius = input("Enter a celsius temperature: ")
        
        # STEP 3 ############################################
        # We need input validation here. We must check the type
        # of the input and determine it is a number.
        # If it is, we can calculate and give the answer
        # if it's not a number, we need to print an error message
        # Hint: you will 'wrap' your conversion code below in an
        #       if/else using the is_number() function from above.
        #
        # DELETE THIS COMMENT BLOCK AFTER YOU ARE
        # DONE CODING AND BEFORE YOU SUBMIT
        # #################################################

        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)

        # STEP 2a: put your previous solution back in place here
        print("")
        print()

    elif choice == "2":
        # choice is 2, ask for and convert fahrenheit_to_celsius
        fahrenheit = input("Enter a fahrenheit temperature: ")

        # STEP 4 ###########################################
        # We need input validation here. We must check the type
        # of the input and determine it is a number.
        # If it is, we can calculate and give the answer
        # if it's not a number, we need to print an error message
        # Hint: you will 'wrap' your conversion code below in an
        #       if/else using the is_number() function from above.
        #
        # DELETE THIS COMMENT BLOCK AFTER YOU ARE
        # DONE CODING AND BEFORE YOU SUBMIT
        # #################################################

        fahrenheit = float(fahrenheit)
        celsius = fahrenheit_to_celsius(fahrenheit)

        # STEP 2b: put your previous solution back in place here
        print("")
        print()

    else:
        print("bye")

# this runs main. i.e. 'calls' main
main()
