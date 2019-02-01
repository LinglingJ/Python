#This program says Hello to the user
import operator
def largest(arr):
    max = 0
    for i in range(1,len(arr)-1):
        if arr[i]>arr[max]:
            max = i
    return max

print('Hello human')
print('Making dictionaries(aka maps) in python')
print('\n...\n')
myFirstDict = {x:0 for x in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
print('Here is the dictionary:')
print(myFirstDict)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
stat_Rel_Freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
print(largest(stat_Rel_Freq))
print(stat_Rel_Freq)
stat_Rel_Freq = sorted(stat_Rel_Freq)
print(stat_Rel_Freq)
# cipher = switch the e and the y
content = 'me namy is jyssica'

#update map with the frequencies of each letter
for char in content:
    if char.upper() in myFirstDict:
        myFirstDict[char.upper()]+=1
print('\n Updated Frequencies:')
print(myFirstDict)

#find highest frequency in content, then next highest and so on...
print('Here is the sorted alphabet')
vv = sorted(myFirstDict.items(),key=operator.itemgetter(1))
print(vv)
print(vv[25][0])   #this gives me the element with the highest frequencies
print(vv[24][0])

#match the highest frequency with the sorted statistical frequency array and
#Write the decoded content
#for index in range(0,25):
#    stat_Map[vv[index][0]]= 




