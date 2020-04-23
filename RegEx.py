# Joe Degere
# 4/23/2020
# Assignment 12- RegEx

import re

# Identifiers
# \d any number
# \D anything but a number
# \s space
# \S anything but a space
# \w any character
# \W anything but a character
# . any character except a new line
# \b the white space around words
# \. period
#
# Modifiers
# {1, 3} expecting 1 - 3
# + match one or more
# * match zero or more
# ^ matches the beginning
# $ matches the end
# ? optional character
# | either or
# [] range or variance
# {x} expecting x amount
#
# White Space Characters
# \n new line
# \s space
# \t tab
# \e escape
# \f form feed
# \r return
#
# DON'T FORGET
# . + * ? [] $ ^ () {} | \

print('It is time to have some programming fun!\n'
      'You will enter a string of your own.\n'
      'You will then proceed to choose one of the numbers below.\n'
      'This will run your string through Regular Expressions.\n'
      'You may begin!\n')


def define(string):
    choice = int(input(""
                       "1.See if the string has a 'q'\n"
                       "2.See if the string contains 'the'\n"
                       "3.See if the string has a '*' in it\n"
                       "4.See if the string contains a digit\n"
                       "5.See if the string contains a period\n"
                       "6.See if the string has at least 2 consecutive vowels (a,e,i,o,u)\n"
                       "7.See if the string contains white space\n"
                       "8.See if the string has any letters that repeat three times in a single word\n"
                       "9.See if the string starts with the word ‘Hello’ (must match the capital H)\n"
                       "10.See if the string contains an email address\n"
                       "11. Print a new string\n"
                       "12.Exit\n>>>"))
    # Find "q" letter
    if choice == 1:
        if re.search(r"q", string):
            return "It contains the letter 'q'\n"
        else:
            return 'The string does not contain the letter "q"\n'
    # Find out if string has "the" word
    if choice == 2:
        if re.search(r'the', string):
            return "It contains 'the'\n"
        else:
            return "The string does not contain 'the'\n"
    # Find * symbol
    if choice == 3:
        if re.search(r'[*]', string):
            return "It contains the star symbol\n"
        else:
            return 'The string does not contain the star symbol\n'
    # Find any digits
    if choice == 4:
        if re.search(r'[0-9]', string):
            return "It contains digits\n"
        else:
            return 'The string does not contain digits\n'
    # Find . in string
    if choice == 5:
        if re.search(r'[.]', string):
            return "It contains a period\n"
        else:
            return 'The string does not contain a period\n'
    # Consecutive letters "aeiou" finder
    if choice == 6:
        if re.search(r'[a,e,i,o,u]{2}', string):
            return "Yes\n"
        else:
            return "No\n"
    # White space
    if choice == 7:
        if re.search(r'[\s]', string):
            return 'The string does contain a white space\n'
        else:
            return 'The string does not contain a white space\n'

    # The string with "Hello"
    if choice == 9:
        if re.search(r'Hello', string):
            return "The string does contain the word 'Hello'\n"
        else:
            return 'The string does not contain the word "Hello"\n'
    # Email @ pattern finder
    if choice == 10:
        if re.findall(r'\w+@\w+\.\w+', string):
            return "This string does contain an email.\n"
        else:
            return 'This string does not contain an email\n'

    if choice == 11:
        print("Ok")

    if choice == 12:
        print('Have a good day!')
        quit()


string = str(input('\n>>>'))
option = None

while option != 0:
    temporary = define(string)
    print(temporary)

    if temporary == None:
        break
