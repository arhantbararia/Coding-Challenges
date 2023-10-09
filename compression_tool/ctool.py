import sys
import os

class HuffBaseNode():
     
     def isLeaf(self) -> bool:
          pass
     

     
     def weight(self) -> int:
          pass
     
     
class HuffLeafNode(HuffBaseNode):
     
    def __init__(self, element , weight) -> None:
        self._element = element
        self._weight = weight
    
    def value(self):
        return self._element
    

    def weight(self):
        return self._weight
    
    def isLeaf():
        return True
    

class HuffInternalNode(HuffBaseNode):
     
    def __init__(self , l , r , weight) -> None:
        self._left = l
        self._right = r
        self._weight = weight
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right
    

    def weight(self) -> int:
        return self._weight
    

    def isLeaf(self) -> bool:
        return False
    

class HuffTree():
    
    def __init__(self , element_or_node , weight = None):
        if weight is not None:
            self._root =HuffLeafNode(element = element_or_node, weight= weight)
        else:
            self._root = element_or_node
    


    def root(self):
        return self._root
    
    def weight(self):
        return self._root
    

    def __lt__(self, other):
        return self._root.weight < other.weight()
    


    
    

    

    

    

    


        



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
    
