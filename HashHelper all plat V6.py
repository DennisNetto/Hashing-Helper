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


# prints the welcome message
def logo():
    print('           //     //         //\\\           /////////    //       //\n           //     //        //  \\\    '
      '     ///           //       //\n           /////////       //====\\\       //////////     ///////////\n      '
      '     //     //      //======\\\            ///      //	  //\n           //     //     //        \\\  '
      '  /////////       //	  //\n\n\n//     //     /////////       ///         ////////////      /////////  '
      '    /////////\n//     //     ///            ///          //        //      ///            ///    //\n/////////  '
      '   /////////     ///           ////////////      /////////      ///    //\n//     //     ///          ///      '
      '      //                ///            ///////////\n//     //     /////////    /////////      //        '
      '        /////////      ///      //\n')


# gets the operation the user wants to do.
def get_switch():
    while True:

        switch = str(input("Press 1 to get a file's hash, Press 2 to compare a file to a hash\n\n:"))

        if switch in ("1", "2"):
            break

        else:
            clear()
            logo()
            print("Error:")
    return(switch)


# If the operation is getting a file hash the user is asked what option they want
def get_method():
    while True:
        
        method = str(input("Press 1 for SHA256, Press 2 for SHA512, Press 3 for MD5\n\n:"))

        if method in ("1", "2", "3"):
            break

        else:
            clear()
            print("Error")
    if method == "1":
        method = "sha256"
    elif method == "2":
        method = "sha512"
    else:
        method = "md5"
    return(method)


# Gets the file location from the user, if its dragged in, the path is modified to work.
def get_file():
     while True:

        try:
            print('What is the file your hashing')
            datain = input("Drag a file into the box or type the path" + "\n\n:")
            if datain[0] == rev and datain[-1] == rev or datain[-1] == " ":
                if operatingsys == "Windows":
                    datain = datain[1:-1]
                else:
                    datain = datain[1:-2]
        except FileNotFoundError:
                print(f"{bcolors.FAIL}(Inncorect path try again){bcolors.ENDC}\n")
        return(datain)
     

# Hashes the file acording to the information provided by the user.
def get_hash(file_path, hash_algorithm, buffer_size=1000000000):
    # Select the hashing algorithm
    if hash_algorithm not in hashlib.algorithms_guaranteed:
        raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")

    # Initialize the chosen hash object
    hash_obj = hashlib.new(hash_algorithm)

    # Read the file in chunks and update the hash object
    with open(file_path, 'rb') as file:
        while chunk := file.read(buffer_size):
            hash_obj.update(chunk)

    # Gets the hexadecimal representation of the hash, and returns it with the algorithm used.
    file_hash = hash_obj.hexdigest()

    return(file_hash, hash_algorithm)



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



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Displays the logo.
method = ''
clear()
logo()

# gets the hashing option from the user.
switch = get_switch()
clear()

# GETTING A HASH FROM A FILE
if int(switch) == 1:

    # Gets the file being used from the user.
    datain = get_file()
    clear()

    method = get_method()
    clear()

    # Hashes the file using the length of the hash given.
    filehash = get_hash(datain, method)

    print(
    " " + f"Method-({bcolors.WARNING}" + filehash[1] + f"{bcolors.ENDC}\n" + F" File path-({bcolors.WAR}" +
    datain +
    f"{bcolors.ENDC}\n" + "\n" + " " + f"{bcolors.ENDC}Hash from File-({bcolors.OKBLUE}" +
    filehash[0], f"{bcolors.ENDC}")



    


# COMPARING A HASH TO A HASH OBTAINED FROM A FILE
if int(switch) == 2:

    clear()
    # gets the comparitive hash from the user.
    testhash = input("Enter the file hash\n\n:")
    testhash = testhash.lower()
    clear()


    # finds the algorithm to use based on how long the hash is
    if len(testhash) == 32:
        method = "md5"
    elif len(testhash) == 64:
        method = "sha256"
    elif len(testhash) == 128:
        method = "sha512"
    

    # Gets the file being used from the user.
    datain = get_file()
    clear()

    # Hashes the file using the length of the hash given.
    filehash = get_hash(datain, method)


    print(
    " " + f"Method-({bcolors.WARNING}" + method + f"{bcolors.ENDC}\n" + F" File path-({bcolors.WAR}" +
    datain + "\n" +
    f"{bcolors.ENDC}\n" + " " + f"{bcolors.ENDC}Hash from File-({bcolors.OKBLUE}" 
    + filehash[0] + "\n" + " " + f"{bcolors.ENDC}Hash from User-({bcolors.HEADER}" + testhash)




