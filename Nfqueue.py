#! /usr/bin/env python

from scapy.all import *

# Man in the Middle with firewall rules
# Test with Raspberry pi #
# Activate the vuln with "iptables -A INPUT -j NFQUEUE --queue-num 0"

from scapy.all import *
    import nfqueue, socket

    def scapy_cb(i, payload):
      s = payload.get_data()  # get and parse the packet
      p = IP(s)

      # Check if the packet is an ICMP Echo Request to 8.8.8.8
      if p.dst == "8.8.8.8" and ICMP in p:
        # Delete checksums to force Scapy to compute them
        del(p[IP].chksum, p[ICMP].chksum)
        
        # Set the ICMP sequence number to 0
        p[ICMP].seq = 0
        
        # Let the modified packet go through
        ret = payload.set_verdict_modified(nfqueue.NF_ACCEPT, raw(p), len(p))
        
      else:
        # Accept all packets
        payload.set_verdict(nfqueue.NF_ACCEPT)

    # Get an NFQUEUE handler
    q = nfqueue.queue()
    # Set the function that will be call on each received packet
    q.set_callback(scapy_cb)
    # Open the queue & start parsing packes
    q.fast_open(2807, socket.AF_INET)
    q.try_run()

