#! /usr/bin/env python

from scapy.all import *

# Envoi d'un segment TCP avec la taille maximale du segment ensemble à 0 à un port spécifique est un test intéressant pour effectuer contre des piles TCP intégrées. Il peut être réalisé avec la seule ligne suivante:

send(IP(dst="1.2.3.4")/TCP(dport=502, options=[("MSS", 0)]))
