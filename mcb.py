#! python3
import pyperclip
import sys
import shelve

mcbFile = shelve.open('mcbFile')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbFile[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbFile.keys())))
    elif sys.argv[1] in mcbFile:
        pyperclip.copy((mcbFile[sys.argv[1]]))
mcbFile.close()