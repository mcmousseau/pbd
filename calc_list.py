#This file contains all functions, including 10 cqlculation functions which can be easily identified by their function names, and a main calculator menu as interface with the users

#a main menu gives an interface to the users to enter an option and the list(s) of numbers, and continue doing so until they wish to quit the program.

#There are two types of operations:
#those involving one list of number - the numbers are either added or multiplied all together (options 1 nd 2) or each number of the list will undergo one separate operation (options 6 to 10)
#those involving two lists of number: the numbers of one list will be used to perform operations on the numbers of the other list (eg substractions  divisions, or power, options 3 to 5)

from functools import reduce
def add (my_list):
    return reduce(lambda a, b: a+b, my_list)

def multiply (my_list):
    return reduce(lambda a, b: a*b, my_list)

def substract (first_list, second_list):
    return list(map(lambda a, b: a-b, first_list, second_list))

def divide (first_list, second_list):
    #return two places decimal if denominator not null or else a message stating can't divide by zero 
    return list(map(lambda a, b: float('%.2f'%(a/b)) if b!=0 else 'division by 0 not allowed', first_list, second_list)) 

def exponent (first_list, second_list):
    return list(map(lambda a, b: a**b, first_list, second_list))

def square (my_list):
    return list(map(lambda a: a*a, my_list))

def squareRoot (my_list):
    #return squqre rrot if positive numer and a message if negative number
    return list(map(lambda a: float('%.2f'%a**0.5) if a>0 else 'a negative number does not have a square root', my_list)) 

def cube (my_list):
    return list(map(lambda a: a**3, my_list))

def factorial (my_list):
    #reduce and map function calculates factorial for each number of the list (x) 
    return list(map(lambda x: (x/abs(x)) * reduce(lambda a, b: a*b, range(1, abs(x)+1)) if x!=0 else 1, my_list))#x/abs(x) allows handling of negative numbers


import math
def cosinus (my_list):
           #return a 2 places decimal number 
    return list(map(lambda a: float('%.2f'%math.cos(a)), my_list))


#The menu function proposse different calculation options and calculate according to the option chosen
def MainMenu ():
    more="c" #the more variable handles the continue or quit  option
    while more == "c":
        print("press 1 to add all numbers from a list")
        print("press 2 to multiply all numbers from a list")
        print("press 3 to substract all numbers from a list by numbers from a second list")
        print("press 4 to divide ll numbers from a list by numbers from a second list")
        print("press 5 to calculate one number from a list to the power of another number from a second list")
        print("press 6 to calculate the square of a list of numbers")
        print("press 7 to calculate the squareRoot of a list of numbers")
        print("press 8 to calculate the cube of a list of numbers")
        print("press 9 to calculate the factorial of a list of numbers")
        print("press 10 to calculate the cosinus of a list numbers")
       # Handling error if no interger is entered
        try:            
            option=int(input())
       #calculation options involving two lists
            if option in  [3, 4, 5]:  
                first_list= list(map(int,input('enter the first list of numbers separated by empty space: ').split()))
                second_list = list(map(int,input('enter the second list of numbers separated by empty space: ').split()))
                if option == 3:
                    result = substract (first_list, second_list)
                elif option == 4:
                    result = divide (first_list, second_list)
                else:
                    result = exponent (first_list, second_list)
            #calculation options involving one list 
            elif option in [1, 2, 6, 7, 8, 9, 10]:
                my_list = list(map(int,input('enter your list of numbers separated by empty space: ').split()))           
                if option == 1:
                    result = add (my_list)
                elif option == 2:
                    result = multiply (my_list)
                elif option == 6:
                    result = square (my_list)
                elif option == 7:
                    result = squareRoot (my_list)
                elif option == 8:
                    result = cube (my_list)
                elif option == 9:
                    result = factorial (my_list)
                else:
                    result = cosinus (my_list)
            
         # returns invalid option if number is outside option range            
            else:                
                result="invalid option"
   # in any case prints result and offers to do another calculation  or to quit  
            print(result)
            more = input("press 'c' if you would like continue; any other key if you would like to quit: ")
   # Handling error if no integer is entered
        except:
             print ("invalid key - please enter the option again!!!!")

    