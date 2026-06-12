from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("\n" + "=" * 50)
    print(f"Packet Number: {packet_count}")

    if IP in packet:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")

        if TCP in packet:
            print("Protocol: TCP")

        elif UDP in packet:
            print("Protocol: UDP")

        print(f"Packet Size: {len(packet)} bytes")

print("Starting Network Sniffer...")
sniff(prn=packet_callback, count=20)

print("\nCapture Completed!")