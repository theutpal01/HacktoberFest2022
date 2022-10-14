#!/usr/bin/python3

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface", dest="interface", help=" whose mac address is being changed")
    parser.add_argument("-m","--mac", dest="new_mac", help=" new mac address")
    args=parser.parse_args()
    if not args.interface:
        parser.error("Please specify an interface, use --help for more info ")
    elif not args.new_mac:
        parser.error("Please specify an interface, use --help for more info ")
    return parser.parse_args()

def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])

def current_mac(interface):
    ifconfig_result=subprocess.run(["ifconfig",interface],capture_output=True)
    mac_address_search_result= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result.stdout))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print(f"couldn't print mac address ")

args= get_arguments()
interface= args.interface
new_mac= args.new_mac
current_mac= current_mac(interface)
print(f"current Mac = "+current_mac )

change_mac(interface,new_mac)
if current_mac(interface)== new_mac:
    print(f"Mac address changed for {interface} to {new_mac}")
else:
    print("Mac address didnot changed")
