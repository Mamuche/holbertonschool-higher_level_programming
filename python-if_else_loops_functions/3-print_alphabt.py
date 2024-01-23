#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue

    print("{:c}".format(letter), end='')
# autre façon de faire :
# for i in range(97, 123):
#    if i == 101 or i == 113:
#        continue
#    print(chr(i), end='')
