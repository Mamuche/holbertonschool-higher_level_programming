#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    new = [i if i != search else replace for i in my_list]
    return new
# line 4 : technique de comprehension de liste
