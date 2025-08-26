from scapy.all import sniff, IP, TCP, UDP, Raw, get_if_list

packets = []

# Callback function when a packet is captured
def packet_callback(pkt):
    packet_data = {
        "src": pkt[IP].src if IP in pkt else None,
        "dst": pkt[IP].dst if IP in pkt else None,
        "proto": pkt.proto if IP in pkt else None,
        "payload": str(bytes(pkt[Raw])[:20]) if Raw in pkt else None
    }
    packets.append(packet_data)

    # Debug print (to confirm capture in terminal)
    if IP in pkt:
        print(f"[+] {pkt[IP].src} -> {pkt[IP].dst} | Proto: {pkt.proto}")

# Function to list all available interfaces
def list_interfaces():
    print("Available interfaces on your system:")
    for iface in get_if_list():
        print(" -", iface)

# Start sniffing on a specific interface
def start_sniffing(iface="Wi-Fi"):
    print(f"[*] Starting packet capture on: {iface}")
    sniff(iface=iface, prn=packet_callback, store=0)
