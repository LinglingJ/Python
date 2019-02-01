#Given an encypted text try to decrypt
import os, sys

def main():
    #Open input file and save into message
    EncryptedFile = 'SomeCipherText.txt'
    if not os.path.exists(EncryptedFile):
        print('------------------------Could not find input file----------------------')
        quit()
    fileObj = open(EncryptedFile)
    content = fileObj.read()
    fileObj.close()
    #Open output file 
    DecryptedFile = 'Decrypted.txt'
    if not os.path.exists(DecryptedFile):
        print('------------------------Could not find output file---------------------')
        quit()
    fileObj_Out = open(DecryptedFile,'w')

    SYMBOLS  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    totalLetters = 0
    thisList = []
    translated = ''

    #Setting the shift key and shifting the letters
    #for key in range(1,26):
    #    count = 0
    key = 18
    for indexOne in range(0,len(content)-1):
        if not SYMBOLS.find(content[indexOne]) == -1:
            newIndex = SYMBOLS.find(content[indexOne]) + key
            if newIndex>25:
                newIndex -=26
            translated = translated + SYMBOLS[newIndex]
        else:
            translated = translated + content[indexOne]
        
    #Printing out the decrypted File.
    fileObj_Out.write(translated)
    fileObj_Out.close()
    print('Done')
    
    print('')
   
main()



