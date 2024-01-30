#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy0 = my_list
    cpy1 = my_list.copy()
    for i in cpy1:
        if idx == cpy1.index(i):
            cpy1.pop(idx)
            cpy1.insert(idx, element)
            return(cpy1)
        elif idx < 0:
            return(cpy1)
        elif idx >= len(cpy1):
            return(cpy1)
