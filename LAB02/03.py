#!/usr/bin/python
import random, string
str = random.sample(string.lowercase + string.digits, 7) + random.sample(string.digits, 1)
random.shuffle(str)
str = ''.join(str)
print str
