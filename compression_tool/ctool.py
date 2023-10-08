import sys
import os




if __name__ == "__main__":

    char_count = {    }

    arguementList = sys.argv[1:]

    count_chars = False
    for argument in arguementList:
        
        
        if argument in ("-m" , '--count_chars'):
            count_chars = True

        if (argument[0] != '-') or (argument[0] != '-' and argument[1] != '-'):
                file_name = argument
                
    try:
        with open(file_name , "r" , encoding="utf8") as file:
            
                for line in file:
                    for char in line:
                        if char not in char_count.keys():
                             char_count[char] = 1
                        else:
                             char_count[char] += 1
                        
                
                    #words = line.split()
                    
        
    except UnicodeDecodeError:
        print("Couldn't decode this line")
    
    except FileNotFoundError:
        print("File not found!")
    
    except NameError:
         print("Enter valid file name.")

    print(char_count)
    
