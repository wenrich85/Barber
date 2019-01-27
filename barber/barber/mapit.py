import webbrowser, sys, pyperclip

# Check for commnd line arguments

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


# https://www.google.com/maps/place/
webbrowser.open('https://www.google.com/maps/place/'+address)


