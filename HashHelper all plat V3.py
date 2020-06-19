import subprocess
import sys
import time
import platform
import hashlib
import os
from os import system, name
from time import sleep


operatingsys = platform.system()
rev = '"'

def clear():

    if operatingsys == "Windows":
        if name == 'nt':
            _ = system('cls')

    else:
        subprocess.run("clear", shell=True)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    WAR = '\033[35m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#The User is prompted to enter the file name, the file hash and what hashing method is to be used.
clear()
print('What is the file your hashing')
x = input("Drag a file into the box or type the path" + "\n\n:")

if x[0] == rev and x[-1] == rev or x[-1] == " ":
    if operatingsys == "Windows":
        x = x[1:-1]
    else:
        x = x[1:-2]


clear()
p = input("Enter the file hash\n\n:")
clear()
y = 0

while y != 1 and y != 2:
    y = int(input("Please pick a hashing function\n 1 for sha256\n 2 for md5\n\n:"))
    clear()

buffer = 262144
md5 = hashlib.md5()
sha256 = hashlib.sha256()


with open(x, 'rb') as f:
    print("Please Wait")
    while True:
        data = f.read(buffer)
        if not data:
            break
        md5.update(data)
        sha256.update(data)


clear()
if y == 1:
    w = format(sha256.hexdigest())
    ww = "sha256"
if y == 2:
    w = format(md5.hexdigest())
    ww = "md5"


BB = str(w)
CC = str(p)

if BB == CC:
    print(f"{bcolors.OKGREEN}-\/(The hashes match, the file is genuine)\/-{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}---!!!(The Hash did not match please check the data, try again if you think this was a mist"
          f"ake)!!!---{bcolors.ENDC}")


z = int(input('Do you want to see the data\n 1 Yes\n 2 No and Exit\n\n :'))

if z == 1:
    BB = BB + "\n"
    CC = CC + "\n"
    print(" " + f"Method-({bcolors.WARNING}" + ww + f"{bcolors.ENDC}\n" + F" File path-({bcolors.WAR}" + x +
          f"{bcolors.ENDC}\n" + "\n" + " " + f"{bcolors.ENDC}Hash from File-({bcolors.OKBLUE}" +
          BB, f"{bcolors.ENDC}Hash from User-({bcolors.HEADER}" + CC)

    input(f"{bcolors.ENDC} press enter to exit")
    clear()
    quit()

if z == 2:
    clear()
    quit()
