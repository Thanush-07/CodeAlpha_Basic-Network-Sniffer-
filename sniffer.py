from scapy.all import sniff 

def call (packet):
    print(packet.show())
sniff(prn=call ,count=5)