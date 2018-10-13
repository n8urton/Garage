#!/usr/bin/env python3

import subprocess, argparse, re

def get_arguments():
    """argument parser"""
    parser = argparse.ArgumentParser(description="Invokes ifconfig to change MAC address of specified network interface")
    parser.add_argument("interface", help="Specify interface for MAC address change")
    parser.add_argument("-m", "--mac", help="Specify new Mac address")
    parser.add_argument("-r", "--restore", help="Restore vendor-specified MAC Address", action="store_true")
    return parser.parse_args()

def subproc_error_msg(cmd, interface, *args):
    """Runs subproccess and returns stdout if successful, prints stderr and exits if not"""
    cmd_list = [cmd, interface] + list(args)
    try:
        return subprocess.check_output(cmd_list, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        error = str(e.stdout.decode("ascii")).rstrip()
        raise SystemExit(f"[-] {cmd}_error '{error}'")

def change_mac(args, current_mac):
    """changes mac address or error message if unsuccessful"""
    #if args.mac != None:
    print(f"[+] Changing {args.interface} MAC address from {current_mac} to {args.mac} ")
    subproc_error_msg("ifconfig", args.interface, "down")
    subproc_error_msg("ifconfig", args.interface, "hw", "ether", str(args.mac))
    subproc_error_msg("ifconfig", args.interface, "up")
    #else:
        #aise SystemExit(f"[-] No MAC address specified. {args.interface} unchanged")

def get_vendor_MAC(args):
    if args.restore:
        ethtool_result = subproc_error_msg("ethtool", "-P", args.interface).decode("ascii")
        mac_search_result = re.search(r"(\w\w:){5}(\w\w)", ethtool_result)
        args.mac = mac_search_result.group(0)
        print(f"[+] Using Vendor Specified MAC address of {args.mac}")
        return args

def get_current_mac(interface):
    ifconfig_result = subproc_error_msg("ifconfig", interface).decode("ascii")
    mac_search_result = re.search(r"(\w\w:){5}(\w\w)", ifconfig_result)

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        #print(f"[-] Interface {interface} has no MAC address (loopback)")
        raise SystemExit(f"[-] Interface {interface} has no MAC address (loopback)")

def main():
    args = get_arguments()
    current_mac = get_current_mac(args.interface)
    get_vendor_MAC(args)
    change_mac(args, current_mac)
    new_mac = get_current_mac(args.interface)
    if new_mac == args.mac:
        print(f"[+] {args.interface} MAC address successfully changed to {new_mac}")
    else:
        print(f"[-] Error, {args.interface} MAC address not set to {args.mac}  Address is currently {new_mac}")

if __name__ == '__main__':
    main()
