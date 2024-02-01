#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy1 = my_list.copy()
    for i in cpy1:
        if idx == cpy1.index(i):
            cpy1.pop(idx)
            cpy1.insert(idx, element)
            return(cpy1)
        elif idx < 0:
            return(my_list)
        elif idx >= len(my_list):
            return(my_list)
