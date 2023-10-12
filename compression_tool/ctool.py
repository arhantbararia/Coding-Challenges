import sys
import os

    
class HuffBaseNode():
     
     def isLeaf(self) -> bool:
          pass
     

     
     def weight(self) -> int:
          pass
     
     
class HuffLeafNode(HuffBaseNode):
     
    def __init__(self, element, weight) -> None:
        self._element = element
        self._weight = weight
    
    def value(self):
        return self._element
    
    def weight(self):
        return self._weight
    
    def isLeaf(self):  # Add "self" parameter
        return True
    
    
    
    

class HuffInternalNode(HuffBaseNode):
     
    def __init__(self, l, r, ) -> None:
        self._left = l
        self._right = r
        self._weight = l.weight() + r.weight()
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right
    
    def weight(self) -> int:
        return self._weight
    
    def isLeaf(self):  # Add "self" parameter
        return False
    
    
    

class HuffTree():
    
    def __init__(self, element_or_node, weight=None):
        print("Tree Building")
        if weight is not None:
            print("weight is not none")
            self._root = HuffLeafNode(element=element_or_node, weight=weight)
        else:
            print("weight is none")
            self._root = element_or_node
    


    def root(self):
        return self._root
    
    def weight(self):
        return self._root.weight()  # Call the weight() method on the root
    
    def __lt__(self, other):
        return self._root.weight() < other.weight()  # Call the weight() method on the root of "other"
    
    def isLeaf(self):
        return self._root.isLeaf()  # Call the isLeaf() method on the root
    
    def __str__(self):
        return self._str_helper(self.root())
    
    def _str_helper(self, node):  ## pre-order Traversal
        if node.isLeaf():
            return f"Leaf({node.value()}, {node.weight()})"
        else:
            left_str = self._str_helper(node.left())
            right_str = self._str_helper(node.right())
            return f"Internal({left_str}, {right_str}, {node.weight()})"
        
    
    def return_huffman_code(self , element):
        code = ''
        return self.huffman_code_helper(self.root(), element, code )
    

    def huffman_code_helper(self , node , element, code):
        
        if node.isLeaf():
            if node.value() == element:
                # print(code)
                # print("element found returning")
                return code
            else:
                # print("not this leaf ", node.value())
                # code += 'X'

                
                return None
            
        else:
            
            
            code += '0'
            left_code = self.huffman_code_helper(node.left() , element , code)
            code = code[:-1]
            if left_code:
                return left_code


            code += '1'
            right_code = self.huffman_code_helper(node.right(), element, code)
            code = code[:-1]
            #print("returning")
            if right_code:
                return right_code
            
            return None




class MinHeap:
    def __init__(self):
        self.heap = []

    

    def push(self, Tree_node):                      # Tree node can be root or leaf
        self.heap.append(Tree_node)
        self._heapify_up(len(self.heap) - 1)

    

    def remove_min(self):
        if not self.heap:
            return None
        
        
        if ( len(self.heap) ==  1):
            return self.heap.pop()
        

        min_element = self.heap[0]

        last_element = self.heap.pop()

        self.heap[0] = last_element
        
        self._heapify_down(0)

        return min_element
    

    def _heapify_up(self, index):
        while (index > 0):
            parent_index = (index-1)//2

            if self.heap[parent_index].weight() > self.heap[index].weight():
                self.heap[parent_index], self.heap[index] = self.heap[index] , self.heap[parent_index] ## swap
                index = parent_index
            else:
                break


    
    def _heapify_down(self, index ):
        left_child_index = 2* index + 1
        right_child_index = 2* index + 2

        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].weight() < self.heap[smallest].weight():
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].weight() < self.heap[smallest].weight():
            smallest = right_child_index
        

        if smallest != index:
            self.heap[index] , self.heap[smallest] = self.heap[smallest] , self.heap[index]
            self._heapify_down(smallest)

    
    



    def heapsize(self):
        return len(self.heap)





def buildTree(min_heap):

    while min_heap.heapsize() > 1 :
        tmp1 = min_heap.remove_min()
        tmp2 = min_heap.remove_min()

        tmp3 = HuffInternalNode(tmp1 , tmp2)
        min_heap.push(tmp3)

    
    return min_heap.remove_min() # return the final internal node




if __name__ == "__main__":

    char_count = { 
        # 'C' : 32, 
        # 'D' : 42, 
        # 'E' : 120,
        # 'K' : 7,
        # 'L' : 42,
        # 'M' : 24,
        # 'U' : 37,
        # 'Z' : 2
       }

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
    print("data stored in dictionary")
    # print(char_count)

    min_heap = MinHeap()

    for element , value in char_count.items():
        new_leaf = HuffLeafNode(element, value)
        min_heap.push(new_leaf)


    # print(min_heap.heap)
    # min_element = min_heap.remove_min()

    # print("Removed minimum element: {min_element}")

    # print(min_heap.heap)

    # print("adding ('$' , 10)" )
    # min_heap.push('$' , 10)

    print("heap created succesfully")

    final_internal_node = buildTree(min_heap)

    huffman_tree = HuffTree(final_internal_node)

    


    prefix_code_table = {}

    for element in char_count.keys():
        prefix_code_table[element] = huffman_tree.return_huffman_code(element)


    print(prefix_code_table)
    

    # leaf_node = HuffLeafNode('a', 5)
    # internal_node = HuffInternalNode(leaf_node, HuffLeafNode('b', 3), 8)
    # huffman_tree = HuffTree(internal_node)
    # print(huffman_tree) 



    
'''
The issue with your huffman_code_helper function is that it doesn't correctly propagate the result back up the recursion stack. 
In Python, when you return a value from a recursive call, you need to capture and return that value in the calling function.
'''