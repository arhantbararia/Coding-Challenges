import sys





if __name__ == "__main__":
    n = len(sys.argv)

    print(n)

    print('arguments passed')
    for i in range(1, n):
        print(sys.argv[i], end = " ")
    
    arguementList = sys.argv[1:]

    count_byte = False   #-c
    count_chars = False  #-m
    count_lines = False #-l
    count_words = False #-w

    #if an argument does not start with '-' or '--' then it is a input file 



    for argument in arguementList:
        if argument in ("-c" , "--count_byte"):
            count_byte = True
        
        if argument in ("-m" , '--count_chars'):
            count_chars = True
        
        if argument in ("-l" , '--count_lines'):
            count_lines = True
    
        if argument in ('-w' , '--count_words'):
            count_words = True
     

        if (argument[0] != '-') or (argument[0] != '-' and argument[1] != '-'):
                file_name = argument


    char_count = 0
    word_count = 0
    line_count = 0
        
    ##opening file
    try:
        with open(file_name , "r") as file:
            

            for line in file:
                line_count += 1
                char_count += len(line)
                words = line.split()
    
    except FileNotFoundError:
        print("File not found!")
    
    except NameError:
         print("Enter valid file name.")

    if(count_chars):
        print(char_count, end= " ")
    
    if(count_lines):
        print(line_count, end= " ")
    if(count_words):
        print(word_count, end= " ")
    
    print(file_name)


    
        


        
