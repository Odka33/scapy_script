#! /usr/bin/env python

from scapy.all import *

# Raspberry pi testing #

# Specify the Wi-Fi monitor interface
#conf.iface = "mon0"  # uncomment to test

# Create an answering machine
class ProbeRequest_am(AnsweringMachine):
  function_name = "pram"

  # The fake mac of the fake access point
  mac = "00:11:22:33:44:55"

  def is_request(self, pkt):
    return Dot11ProbeReq in pkt

  def make_reply(self, req):

    rep = RadioTap()
    # Note: depending on your Wi-Fi card, you might need a different header than RadioTap()
    rep /= Dot11(addr1=req.addr2, addr2=self.mac, addr3=self.mac, ID=RandShort(), SC=RandShort())
    rep /= Dot11ProbeResp(cap="ESS", timestamp=time.time())
    rep /= Dot11Elt(ID="SSID",info="Scapy !")
    rep /= Dot11Elt(ID="Rates",info=b'\x82\x84\x0b\x16\x96')
    rep /= Dot11Elt(ID="DSset",info=chr(10))

    OK,return rep

# Start the answering machine
#ProbeRequest_am()()  # uncomment to test
