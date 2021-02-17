#! /usr/bin/env python

# importing modules
import scapy.all as scapy
import optparse
import re
import ipaddress


# allows user to add arguments THROUGH the command line
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--t", "--target", dest="target", help="Specifying the target IP")
    (option, arguments) = parser.parse_args()
    if ipaddress.ip_network(option.target, False):
        return option.target
    else:
        print('[-] Please type a valid IP!')


# scan function scans the ip address given by the user to get the MAC address
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request
    arp_broadcast.show()
    answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].pdst, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


# prints the list of the total IPs and MACs on the network.
def print_result(results_list):
    number = 0
    print("IP\t\t\t\t\tMAC")
    for client in results_list:
        number += 1
        print(str(number) + ". " + client["ip"] + "\t\t\t" + client["mac"])
        print("--------------------------------------")
    return results_list


options = get_arguments()
scan(options)
print_result(scan_ip)
