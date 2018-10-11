#------------------------------------------------------------------------------#
# (c) 2018 Uzair Tariq
# Text to array program
# Paste in your long list of text, with all seperate words seperated with a
# space
#------------------------------------------------------------------------------#
import clipboard

print("(c) 2018 Uzair Tariq \nPlain text to array program \n")

string_or_not = input("Would you like the objects in your array to be converted into strings? (y/n) ")

plain_text = ''

plain_text = input("\nPaste your text here. Make sure to seperate seperate items with a space between them: \n")

if string_or_not == 'y':
    plain_text = plain_text.replace(" ", "', '")
else:
    plain_text = plain_text.replace(" ", ", ")

print("\nHere's your array: \n")

if string_or_not == 'y':
    array = "['" + plain_text + "']"
else:
    array = '[' + plain_text + ']'

print(array)

copy = input("\nWould you like to copy the result? (y/n) ")

if copy == 'y':
    clipboard.copy(array)
    print("\nCopied to clipboard! \n")
elif copy == 'n':
    '\n'
