#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

# Importing all the necessary Libraries.
import webbrowser # Used for opening google maps website
import sys # For Retrirving the address from the commandline
import pyperclip # To Retrieve the address from the clipboard.

# get the address from either the command line or clipboard.
if len(sys.argv) > 1:
    # Get address from the command line
    ## As the sys.argv[0] is the program name
    addr = ' '.join(sys.argv[1:])

# Get the address from teh clipboard if the address 
# is not passed as an argument in the commandline.
else:
    addr = pyperclip.paste() 


# pyperclip.copy('870 Valencia St, San Francisco, CA 94110')
# addr = pyperclip.paste() 

# 
address = addr.replace(',', '').split(' ')
webbrowser.open('https://www.google.com/maps/place/'+ str('+'.join(address)) + '/')