#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    """argument parser"""
    parser = argparse.ArgumentParser(description="Broadcasts ARP request to specified IP range for network discover")
    parser.add_argument("target", help = "Specify IP range to scan")
    return (parser.parse_args())

def scan(ip):
    """arp request"""
    # scapy.arping(ip) # scapy.arping does
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast destination mac address
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1)
    #print(answered_list.summary())
    clients_list = []
    for element in answered_list:
        #print(element[1].show()) #shows human readable packet info
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwdst)
    return (clients_list)

def print_result(results_list):
    print("IP\t\t\tMAC Addres\n.........................................")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

args = get_arguments()
scan_result = scan(args.target)
print_result(scan_result)