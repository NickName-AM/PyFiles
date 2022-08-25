import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int,help="Number of files to create (Default: 10)")
parser.add_argument("-e", "--extension", type=str, help="Extension of file (Default: txt)")
args = parser.parse_args()

number = args.number or 10
ext = args.extension or 'txt'

b = "abcdefghijklmnopqrstuvwxyz"
c = b.upper() + "0123456789"
a = b + c

for i in range(number):
    n = random.choice(range(9,12))
    name = "".join(random.choices(a,k=n))
    open(f"{name}.{ext}", 'w').close()
