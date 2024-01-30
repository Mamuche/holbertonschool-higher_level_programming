#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if idx == my_list.index(i):
            my_list.pop(idx)
            my_list.insert(idx, element)
            return(my_list)
        elif idx < 0:
            return(my_list)
        elif idx >= len(my_list):
            return(my_list)
