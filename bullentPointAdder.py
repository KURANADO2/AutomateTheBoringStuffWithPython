#! python3
import pyperclip

text = pyperclip.paste();
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
print(text)
# Test data
# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivate
