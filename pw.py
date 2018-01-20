#! python3
import sys
import pyperclip

PASSWORDS = {'email': 'ASKDLJAGFLRGEIAOL',
             'blog': 'jfoi1345dsa2398r',
             'luggage': '123456'}


if len(sys.argv) <= 1:
    print('Usage: py pw.py [account] - copy account password.')
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + '.')
