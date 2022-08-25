import os
import random

ext = 'txt'

b = "abcdefghijklmnopqrstuvwxyz"
c = b.upper() + "0123456789"
a = b + c

for i in range(20):
    n = random.choice(range(9,12))
    name = "".join(random.choices(a,k=n))
    open(f"{name}.{ext}", 'w').close()
