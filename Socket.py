#! /usr/bin/env python

from scapy.all import *
import socket

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create an UDP socket
sck.connect(("8.8.8.8", 53))  # connect to 8.8.8.8 on 53/UDP

# Create the StreamSocket and gives the class used to decode the answer
ssck = StreamSocket(sck)
ssck.basecls = DNS

# Send the DNS query
ssck.sr1(DNS(rd=1, qd=DNSQR(qname="www.example.com")))
