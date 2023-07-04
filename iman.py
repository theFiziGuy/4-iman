import os 
import time 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN + "Hello Iman its me abby......." + bcolors.BOLD)
time.sleep(5)
print(bcolors.WARNING + "I know its u (: " + bcolors.ENDC)
time.sleep(1.2)
print(bcolors.HEADER + "opssssss" + bcolors.ENDC)
time.sleep(1.4)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.5)
print(bcolors.OKGREEN + "Downloading Information.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Downloading Longitude.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Getting Ip .." + bcolors.BOLD)
print(bcolors.OKGREEN + "Getting Passwords.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Downloading Contacts.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Bye -Abby." + bcolors.BOLD)
