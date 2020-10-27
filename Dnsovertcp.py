#! /usr/bin/env python

import socket
from scapy.all import *

# Make a DNS over TCP request with a socket wait the response to print the result.

class DNSTCP(Packet):
    name = "DNS over TCP"
    
    fields_desc = [ FieldLenField("len", None, fmt="!H", length_of="dns"),
                    PacketLenField("dns", 0, DNS, length_from=lambda p: p.len)]
    
    # This method tells Scapy that the next packet must be decoded with DNSTCP
    def guess_payload_class(self, payload):
        return DNSTCP

# create an TCP socket
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect(("8.8.8.8", 53))  # connect to 8.8.8.8 on 53/TCP

# Create the StreamSocket and gives the class used to decode the answer
ssck = StreamSocket(sck)
ssck.basecls = DNSTCP

# Send the DNS query
ssck.sr1(DNSTCP(dns=DNS(rd=1, qd=DNSQR(qname="www.example.com"))))
