#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = [x for x in set_1 and set_2 if x not in set_2 or x not in set_1]
    return res