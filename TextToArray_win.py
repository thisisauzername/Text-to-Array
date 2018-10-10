#------------------------------------------------------------------------------#
# (c) 2018 Uzair Tariq
# Text to array program
# Paste in your long list of text, with all seperate words seperated with a
# space
#------------------------------------------------------------------------------#
import sys
import subprocess

def write_to_clipboard(output):
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        subprocess.Popen(['clip'], stdin=subprocess.PIPE).communicate(output)
    else:
        raise Exception('Platform not supported')

print("(c) 2018 Uzair Tariq \nPlain text to array program \n")

plain_text = ''

plain_text = input("Paste your text here. Make sure to seperate seperate items with a space between them: \n")

plain_text = plain_text.replace(" ", ", ")

print("\nHere's your array: \n")

array = '[' + plain_text + ']'

print(array)

copy = input("\nWould you like to copy the result? (y/n) \n")

if copy == 'y':
    write_to_clipboard(array)
    print("\nCopied to clipboard! \n")
elif copy == 'n':
    '\n'
