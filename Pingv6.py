#! /usr/bin/env python

from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="A simple ping6")
parser.add_argument("ipv6_address", help="An IPv6 address")
args = parser.parse_args()

print(sr1(IPv6(dst=args.ipv6_address)/ICMPv6EchoRequest(), verbose=0).summary())
