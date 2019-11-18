# John Henke
# CSCI 102 - Section A
# Week 12 - Utility

def PrintOutput(string):
    print("OUTPUT", string)

def LoadFile(string):
    list_of_lines = []
    with open (string, 'r') as file:
        for line in file:
            line_temp = line
            list_of_lines.append(line_temp)
    return list_of_lines

def UpdateString(string, replacement, index):
    list_string = [i for i in string]
    list_string[index] = replacement
    final_string = ''
    for i in list_string:
        final_string += i
    print("OUTPUT", final_string)

def FindWordCount(given_list, string):
    counter = 0
    for word in given_list:
        if word == string:
            counter += 1
    return counter


            
    
    


        



