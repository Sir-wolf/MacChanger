"""Import modules"""

import re

import subprocess

from random import choice, randint, shuffle

import optparse

import os

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
shuffle(color_random)

maclogo = color_random[0] + '''
███╗   ███╗ █████╗  ██████╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██║     ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║     ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║╚██████╗╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                      
        ''' + color.END
macPrompt = "MacChanger ~# "




def clearScr():
    os.system('clear')

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(color.NOTICE + "[-] Please specify the interface, use --help for more info" + color.END)
    return options

options = get_arguments()
clearScr()



print (maclogo + color.RED + '''
       }--------------{+} Coded By Sirwolf {+}--------------{
       }--------{+}    GitHub.com/Sir-wolf :)    {+}--------{
    ''' + color.END)
print(color.OKGREEN + "\n [*] Enter 1 for manual change of mac adress and 2 for random mac adress: " + color.END)
inp = input(macPrompt)
interface = options.interface

def mac_random():
    """Generate a random MAC address taking the first 3 pairs from
Cisco and Dell defined hardware, and generate the 3 last pairs randomly"""
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)


def change_mac(interface, new_mac):
    """Use Linux commands to change the mac"""
    print(color.HEADER + "[+] Changing MAC address for " + str(interface) + " ! "+ color.END)
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " hw ether " + str(new_mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)



def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print(color.WARNING + "[-] Could not read MAC address." + color.END)

current_mac = get_current_mac(options.interface)

clearScr()
print(color.NOTICE + "[+] Current MAC is "+ str(current_mac) + color.END)

random = mac_random()

def main():
    if inp == "1":
        if not options.new_mac:
            parser = optparse.OptionParser()
            parser.error(color.WARNING + "[-] Please specify the new MAC, use --help for more info" + color.END)
        else: 
            change_mac(interface, options.new_mac)

    elif inp == "2":
        change_mac(interface, random)

if (current_mac == options.new_mac or random):

    print(color.OKBLUE + "[+] MAC address was successfully changed to " + str(options.new_mac) + " or to " + str(random) + color.END)
else:
    print(color.WARNING + "[-] MAC address did not changed." + color.END)

if __name__ == '__main__':
    main()
