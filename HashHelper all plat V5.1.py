import subprocess
import platform
import hashlib
from os import system, name


# Variable declaration
# File input = data-in
# File hash  = test-hash
# Hash method = method-pick
# File after hash = data-out
# method used to hash = method
# information and quit or quit = done


# Gains the type of operating system.
operatingsys = platform.system()
rev = '"'


# Uses the operating system to define the method of clearing the shell.
def clear():

    if operatingsys == "Windows":
        if name == 'nt':
            _ = system('cls')

    else:
        subprocess.run("clear", shell=True)


# Formatting information.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    WAR = '\033[35m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'


# The User is prompted to enter the file name, the file hash and what hashing method is to be used.
contin = 1
clear()
print('           //     //         //\\\           /////////    //       //\n           //     //        //  \\\    '
      '     ///           //       //\n           /////////       //====\\\       //////////     ///////////\n      '
      '     //     //      //======\\\            ///      //	  //\n           //     //     //        \\\  '
      '  /////////       //	  //\n\n\n//     //     /////////       ///         ////////////      /////////  '
      '    /////////\n//     //     ///            ///          //        //      ///            ///    //\n/////////  '
      '   /////////     ///           ////////////      /////////      ///    //\n//     //     ///          ///      '
      '      //                ///            ///////////\n//     //     /////////    /////////      //        '
      '        /////////      ///      //\n')
while contin == 1:
    # finds if the user wants a hash or is comparing a file to a hash.
    switch = 0
    while switch != 1 and switch != 2:
        switch = int(input("Press 1 to get a file's hash, Press 2 to compare a file to a hash\n\n:"))
        clear()
        while True:
            try:
                print('What is the file your hashing')
                datain = input("Drag a file into the box or type the path" + "\n\n:")
                # Uses the file input to asses if its a typed input or dragged auto input.
                if datain[0] == rev and datain[-1] == rev or datain[-1] == " ":
                    if operatingsys == "Windows":
                        datain = datain[1:-1]
                    else:
                        datain = datain[1:-2]
                # Gets a hash if the user wants to compare.
                if switch == 2:
                    clear()
                    # The user is prompted to enter the hash to be tested with the file hash
                    testhash = input("Enter the file hash\n\n:")

                clear()
                methodpick = 0
                # Makes the user pick a method.
                while methodpick != 1 and methodpick != 2:
                    methodpick = int(input("Please pick a hashing function\n 1 for sha256\n 2 for md5\n\n:"))
                    clear()
                # Sets up a buffer to stop over use of ram capped at 1GB.
                buffer = 1000000000
                # Sets up the hashing algorithm.
                if methodpick == 2:
                    md5 = hashlib.md5()
                if methodpick == 1:
                    sha256 = hashlib.sha256()

                # Reads the buffer and updates the hashing method.
                with open(datain, 'rb') as f:
                    print("Please Wait")
                    while True:
                        data = f.read(buffer)
                        if not data:
                            break
                        if methodpick == 2:
                            md5.update(data)
                        if methodpick == 1:
                            sha256.update(data)

                clear()
                # Takes the indicated method and outputs the chosen data.
                if methodpick == 1:
                    dataout = str(format(sha256.hexdigest()))
                    method = "sha256"
                if methodpick == 2:
                    dataout = str(format(md5.hexdigest()))
                    method = "md5"
                # If the user wanted a hash its printed for them.
                break
            except FileNotFoundError:
                print(f"{bcolors.FAIL}(Inncorect path try again){bcolors.ENDC}\n")

    if switch == 1:
        print(
            " " + f"Method-({bcolors.WARNING}" + method + f"{bcolors.ENDC}\n" + F" File path-({bcolors.WAR}" + datain +
            f"{bcolors.ENDC}\n" + "\n" + " " + f"{bcolors.ENDC}Hash from File-({bcolors.OKBLUE}" +
            dataout + "\n")
        loop = 0
        while loop != 1 and loop != 2:
            loop = int(input(f"{bcolors.ENDC} press 1 to hash another file press 2 to exit \n\n:"))
            if loop == 1:
                contin = 1
                clear()

            if loop == 2:
                clear()
                quit()
    # If the user wanted to compare hashes they are compared and returned.
    if switch == 2:
        # If the file hash matches the given hash it out puts genuine if not it alerts the user to the mistake.
        if dataout == testhash:

            print(f"{bcolors.OKGREEN}-\/(The hashes match, the file is genuine)\/-{bcolors.ENDC}")
        else:
            print(
                f"{bcolors.FAIL}---!!!(The Hash did not match please check the data, try again if you think this "
                f"was a mist"
                f"ake)!!!---{bcolors.ENDC}")

        # allows the user a chance to see the data if desired.
        done = int(input('Do you want to see the data\n 1 Yes\n 2 No. Hash another file\n 3 Exit\n\n :'))
        # Prints the data and exits.
        if done == 1:
            dataout = dataout + "\n"
            testhash = testhash + "\n"
            print(
                " " + f"Method-({bcolors.WARNING}" + method + f"{bcolors.ENDC}\n" + F" File path-({bcolors.WAR}" +
                datain +
                f"{bcolors.ENDC}\n" + "\n" + " " + f"{bcolors.ENDC}Hash from File-({bcolors.OKBLUE}" +
                dataout, f"{bcolors.ENDC}Hash from User-({bcolors.HEADER}" + testhash)
        loop = 0
        while loop != 1 and loop != 2:
            loop = int(input(f"{bcolors.ENDC} press 1 to hash another file press 2 to exit \n\n :"))
            if loop == 1:
                contin = 1
                clear()

            if loop == 2:
                clear()
                quit()

        if done == 2:
            contin = 1
            clear()

        # Exits.
        if done == 3:
            clear()
            quit()
