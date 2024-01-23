#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
   print("{:c}".format(i), end="")
# autre façon de faire :
#
# for i in range(97, 123):
#    print(chr(i), end='')
