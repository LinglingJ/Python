#Reverse Cipher
import pyperclip
note = 'Hello, this is the computer speaking or is it?'
message = ''
i = len(note)-1
while i>=0:
    message = message + note[i]
    i=i-1
print(message)
pyperclip.copy(message)

