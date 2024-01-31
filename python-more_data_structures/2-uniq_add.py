#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_add = sum(set(my_list))
    return new_add
# set - convertit la liste en un ensemble,
# qui ne permet pas d'avoir un element en double
