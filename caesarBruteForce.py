#Decrypting


#Open and Read File
EncryptedFile = 'SomeCipherText.txt'
if not os.path.exists(EncryptedFile)
    print('Could not find file.... Quiting..')
    quit()
FileObj = open(EncryptedFile)
contents = FileObj.read()


#Re-arrange contents based off of a key
key = 1
while(not contents.eof())
    

#Write it out to a file called decryptedContents


