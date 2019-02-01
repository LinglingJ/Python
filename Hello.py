#To run a python program 
# 1. go to the command window
# 2. Navigate to directory of python file
# 3. Type: Python Hello.Py
#
import random

print ("My world.")

for i in range (0,3):
    Pass = input("Enter password:")
    if (Pass=="Frog") or (Pass=="frog"):
        accept = 1
        break
    i=i+1
if accept==1:
    print("1 2 3 4 5")
    num=int(input("What would you like to do? "))
    #define the function blocks
    #Note: it does not perform the def unless they are called on
    def one():
        print("\tPlay video games")
    def two():
        print("\tGo to the park")
    def three():
        print("\tGo do your hobby")
    def four():
        print("\tDo homework")
    def five():
        num = random.randint(2,4)
        options[num]()
    #map the inputs to the function blocks
    options ={
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,        
    }
    options[num]()
   





