#Character Substitution encryption and decryption code
import os, sys
import operator

def main():
    
    #In_File = 'TheAdventures.txt'
    In_File = 'Out_Contents.txt'
    Out_File = 'Decrypted.txt'
    #Open file and save into message
    if not os.path.exists(In_File):
        print('Could not find input file...')
        quit()
    fileObj1 = open(In_File)
    content = fileObj1.read()
    fileObj1.close()
    #Open output file
    if not os.path.exists(Out_File):
        print('Could not find output file...')
        quit()
    fileObj2 = open(Out_File,'w')
    


    #Declaring Variables
    totalLetters = 0
    thisList = []
    SYMBOLS  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stat_Rel_Freq = [8.167,1.492,2.782,4.253,12.702,2.228,
                    2.015,6.094,6.966,0.153,0.772,4.025,2.406,
                    6.749,7.507,1.929,0.095,5.987,6.327,9.056,
                    2.758,0.978,2.360,0.150,1.974,0.074]
    stat_Dict = {x:stat_Rel_Freq[ord(x)-ord('A')] for x in (SYMBOLS)}
    content_Dict = {x:0 for x in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    sorted_Stat_Dict = sorted(stat_Dict.items(),key=operator.itemgetter(1))
    key = 'wbphqgiumeaylnofdxjkrcvstz'
    translated = ''


    #Decide if you are encrypting or decrypting
    print('Would you like to encrypt or decrypt? Press E or D and then hit enter')
    crypt = input()

    if not ((crypt.upper() == 'E') or (crypt.upper() == 'D')):
        print('Next time enter in either "E" or "D" for encrypting or decrypting')
        quit()

    if crypt.upper() == 'E':
        print('Encrypting...')
        for character in content:
            if not SYMBOLS.find(character.upper())== -1:
                translated = translated + key[SYMBOLS.find(character.upper())]
            else:
                translated = translated + character
    else:
        print('Do you want to decrypt using letter frequencies? Enter Y or N ')
        LetterFreq = input()
        if not ((LetterFreq.upper() == 'Y') or (LetterFreq.upper() =='N')):
            print('Next time enter Y or N')
            quit()
        print('Decrypting...')
        
        if LetterFreq.upper() == 'Y':
            #Decrypt using letter frequencies
            #Find the Frequency in the content

            for character in content:
                if character.upper() in content_Dict:
                    content_Dict[character.upper()] += 1
            sorted_Content_Dict = sorted(content_Dict.items(),key=operator.itemgetter(1))
            #Assign the "real" letters
            dict_mapping = {}
            for iterator in range(0,26):
                dict_mapping[sorted_Content_Dict[iterator][0]] = sorted_Stat_Dict[iterator][0]
            #print('sorted stat dict:')
            #print(sorted_Stat_Dict)
            #print('sorted content dict')
            #print(sorted_Content_Dict)
            #print('put together')
            #print(dict_mapping)
            for character in content:
                if character.upper() in SYMBOLS:
                    translated = translated + dict_mapping[character.upper()]
                else:
                    translated = translated + character


        else:
            for character in content:
                if not key.find(character)== -1:
                    translated = translated + SYMBOLS[key.find(character)]
                else:
                    translated = translated + character
            
    fileObj2.write(translated)
    fileObj2.close()


    
    print('')
    
    print('Done')
    
main()






