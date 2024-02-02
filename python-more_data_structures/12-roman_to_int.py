#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (roman_string):
        return (0)
    if type(roman_string) != str:
        return (0)

    numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    pre = 0
    sum = 0

    for i in roman_string:
        sum += numbers[i] if numbers[i] <= pre else numbers[i] - pre * 2
        pre = numbers[i]
    return sum
