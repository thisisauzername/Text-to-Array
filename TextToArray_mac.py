#------------------------------------------------------------------------------#
# (c) 2018 Uzair Tariq
# Text to array program
# Paste in your long list of text, with all seperate words seperated with a
# space
#------------------------------------------------------------------------------#
import subprocess

# Write to clipboard function
def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

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
    ''
