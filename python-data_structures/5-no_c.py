#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    while 'c' in char_list:
        char_list.remove('c')
    while 'C' in char_list:
        char_list.remove('C')
    result = ''.join(char_list)
    return result
