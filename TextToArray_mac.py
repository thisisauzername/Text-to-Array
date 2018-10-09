#------------------------------------------------------------------------------#
# (c) 2018 Uzair Tariq
# Text to array program
# Paste in your long list of text, with all seperate words seperated with a
# space
#------------------------------------------------------------------------------#
import os

def write_to_clipboard(data):
    os.system("echo '%s' | pbcopy" % data)

print("(c) 2018 Uzair Tariq \nPlain text to array program \n")

input = ''

input = raw_input("Paste your text here. Make sure to seperate seperate items with a space between them: \n")

input = input.replace(" ", ", ")

print("\nHere's your array: \n")

array = '[' + input + ']'

print(array)

copy = raw_input("\nWould you like to copy the result? (y/n) \n")

if copy == 'y':
    write_to_clipboard(array)
    print("\nCopied to clipboard! \n")
elif copy == 'n':
    ''
