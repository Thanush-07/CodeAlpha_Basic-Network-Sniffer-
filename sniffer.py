from scapy.all import sniff, get_if_list
import threading
import json

packets = []

def packet_callback(packet):
    try:
        src = packet[0][1].src if hasattr(packet[0][1], "src") else "N/A"
        dst = packet[0][1].dst if hasattr(packet[0][1], "dst") else "N/A"
        proto = packet[0][1].name if hasattr(packet[0][1], "name") else "N/A"
        payload = bytes(packet.payload)[:50].hex()  # small preview
    except Exception as e:
        src, dst, proto, payload = "N/A", "N/A", "N/A", str(e)

    packets.append({
        "src": src,
        "dst": dst,
        "proto": proto,
        "payload": payload
    })

    # keep only last 50 packets
    if len(packets) > 50:
        packets.pop(0)


def get_default_iface():
    """Pick the first non-loopback interface automatically"""
    interfaces = get_if_list()
    for iface in interfaces:
        if not iface.startswith("lo"):  # skip loopback
            return iface
    return interfaces[0]  # fallback


def start_sniffing():
    iface = get_default_iface()
    print(f"[*] Starting packet capture on: {iface}")
    sniff(iface=iface, prn=packet_callback, store=0)
