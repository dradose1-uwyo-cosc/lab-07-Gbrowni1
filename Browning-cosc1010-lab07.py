# Grant Browning
# UWYO COSC 1010
# 10/31/2024
# Lab 7
# Lab Section: 13?
# Sources, people worked with, help given to: https://www.w3schools.com/python/ref_string_split.asp, https://docs.python.org/3/genindex-Symbols.html

# Code works and outputs values properly, except I cannot "exit" the 3rd part. Error messages claims it is something to do
# with line 119, op1 = int(input_str[0]) but my done message should catch the code before then.

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
upper_bound = ""
while True:
    upper_bound = input("Enter the upper bound of the factorial: ") #Factorial number (X!)

    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        break
    else:
        print("Symbol is not a number, please enter a number")

factorial = 1
placeholder = upper_bound #n-1 to continue loop until *1

while placeholder >= 1:
    factorial = factorial * placeholder
    placeholder -= 1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

ns_sum = 0

while True:
    ns_input = (input("Please enter numbers you would like to add, one number at a time('exit' to exit): "))
    
    if ns_input.upper() == "EXIT":
        break

    if ns_input.isdigit():
        ns_input = int(ns_input)
        ns_sum += ns_input

    elif ns_input[0] == "-":

        ns_input = ns_input.replace('-', "")
        if ns_input.isdigit():
            ns_input = int(ns_input)
            ns_sum = ns_sum - ns_input
    
    else:
        print("Unnacceptable input, please enter a number")

print(f"Your final sum is {ns_sum}")

print("*"*75)

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

op1 = 0
op2 = 0
answer = 0

while True:
    calc_input = (input("Please enter your desired 2-integer math problem('exit' to exit):"))
    
    if calc_input.upper == "EXIT":
        break
    
    import re

    if input:
        if calc_input.upper == "EXIT":
            break

        input_str = re.split("[+-/*%]", calc_input)

        if input_str[0].upper == "EXIT":
            break

        if input_str[0].isdigit:
                op1 = int(input_str[0])  #Code does not like something about 'exit' and this line, I don't know why.

        if input_str[-1].isdigit:
                op2 = int(input_str[-1])
        else:
             print("Unnacceptable format")

    for symbol in calc_input:

        if "+" in calc_input:
            answer = op1 + op2

        if "-" in calc_input:
            answer = op1 - op2

        if "/" in calc_input:
            answer = op1 / op2
        
        if "*" in calc_input:
            answer = op1 * op2

        if "%" in calc_input:
            answer = op1 % op2
        
    else:
            print("Unnacceptable input, please enter a number")
 
    print(f"The answer is: {answer}")

print("Code finished")