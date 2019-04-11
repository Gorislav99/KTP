#!/usr/bin/python
import random, string
str = random.sample(string.lowercase + string.digits, 7) + random.sample(string.digits, 1)
random.shuffle(str)
str = ''.join(str)
print "str: ", str
str_alpha = ''
str_digit = ''
for s in str:
    if s in string.digits:
        str_alpha = str_alpha + s
    else:
        str_digit = str_digit + s
print "str_alpha: " , str_alpha
print "str_digit: " , str_digit
