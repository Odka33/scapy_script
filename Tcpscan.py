#! /usr/bin/env python

from scapy.all import *

class TCPScanner(Automaton):

    @ATMT.state(initial=1)
    def BEGIN(self):
        pass

    @ATMT.state()
    def SYN(self):
        print("-> SYN")

    @ATMT.state()
    def SYN_ACK(self):
        print("<- SYN/ACK")
        raise self.END()

    @ATMT.state()
    def RST(self):
        print("<- RST")
        raise self.END()

    @ATMT.state()
    def ERROR(self):
        print("!! ERROR")
        raise self.END()
    @ATMT.state(final=1)
    def END(self):
        pass
    
    @ATMT.condition(BEGIN)
    def condition_BEGIN(self):
        raise self.SYN()

    @ATMT.condition(SYN)
    def condition_SYN(self):

        if random.randint(0, 1):
            raise self.SYN_ACK()
        else:
            raise self.RST()

    @ATMT.timeout(SYN, 1)
    def timeout_SYN(self):
        raise self.ERROR()

TCPScanner().run()
