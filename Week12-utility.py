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
    return PrintOutput(list_of_lines)
        



