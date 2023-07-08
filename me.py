import os 
import time 
import socket 
from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)
iman = "+60176260121"
me = "+60163463960"
fake_ip = fake.ipv4_private()

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

HostName = socket.gethostname()
IPAdrees = socket.gethostbyname(HostName)


print(bcolors.OKCYAN + "Hello Iman its me abby......." + bcolors.BOLD)
time.sleep(5)
print(bcolors.WARNING + "I know its u (: " + bcolors.ENDC)
time.sleep(3)
print(bcolors.HEADER + "opssssss" + bcolors.ENDC)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.5)
print(bcolors.OKGREEN + "Downloading Information.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Downloading Longitude.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Getting Ip .." + bcolors.BOLD)
print(bcolors.OKGREEN + "Getting Passwords.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Downloading Contacts.." + bcolors.BOLD)
print(bcolors.OKGREEN + "Bye -Abby." + bcolors.BOLD)
time.sleep(2)
print(bcolors.WARNING + "You just got pranked xd xd." + bcolors.BOLD)
time.sleep(2)
print(bcolors.WARNING + "sorry." + bcolors.BOLD)
time.sleep(5)
countinueInput = input(bcolors.OKGREEN + "Do You want to countinue? Yes/No" + bcolors.BOLD)

if countinueInput == "Yes" or "yes" or "y" or "Y":
    print(bcolors.OKGREEN + "lets see" )
    print("Your Ip Is " + fake_ip +  "And your number is" +iman+ "Thx Iman")
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    print(bcolors.OKCYAN + "ok dah")


elif  countinueInput == "No" or "no" or "n" or "N":
        print(bcolors.OKGREEN + "Your Ip Is " + IPAdrees)
        print(bcolors.OKGREEN + "Downloading Information.." + bcolors.BOLD)
        print(bcolors.OKGREEN + "Downloading Longitude.." + bcolors.BOLD)
        print(bcolors.OKGREEN + "Getting Ip .." + bcolors.BOLD)
        print(bcolors.OKGREEN + "Getting Passwords.." + bcolors.BOLD)
        print(bcolors.OKGREEN + "Downloading Contacts.." + bcolors.BOLD)
        print("Your Ip Is " +fake_ip + "OWOWOWO")

else:
        print("Please Try Again")
