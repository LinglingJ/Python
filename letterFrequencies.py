#Counting the frequencies in Mark Twain's book

#Finding and Opening the file
import time, os, sys

def main():
    inputFile = 'TheAdventures.txt'
    if not os.path.exists(inputFile):
        print('The file %s does not exist. Quitting...'%(inputFile))
        sys.exit()
    Letters = 'abcdefghijklmnopqrstuvwxyz'
    fileObj = open(inputFile)
    content = fileObj.read()
    content
    print('The actual letter frequencies:')
    print('')
    fileObj.close()
    totalLetters = 0
    thisList = []
    stat_Rel_Freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
    #[11.682, 4.434, 5.238, 3.174, 2.799, 4.027, 1.642, 4.200, 7.294, 0.511, 0.456, 2.415, 3.826, 2.284, 7.631, 4.319, 0.222, 2.826, 6.686, 15.978, 1.183, 0.824, 5.497, 0.045, 0.763, 0.045]
    print('Letter | Actual Freq | Expected Freq | Actual Rel Freq | Expected Rel Freq')
    for indexTwo in range(0,len(Letters)):
        count = 0
        for indexOne in range(0,len(content)-1):
            if content[indexOne].lower()==Letters[indexTwo]:
                count=count+1
        totalLetters = totalLetters + count
        thisList.insert(indexTwo,count)
    aa = 0
    for indexList in thisList:
        print('   '+Letters[aa]+'   | %11d' % indexList, '| %12d' % (totalLetters*stat_Rel_Freq[aa]/100.0), ' | %14f' % (100*indexList/float(totalLetters)),' | %15f' % stat_Rel_Freq[aa])
        aa = aa+1
        
    print('The total amount of letters is',totalLetters)
    
    print('')
    
    print('The expected and actual frequency seem to be pretty close as expected')
    
main()

