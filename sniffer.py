from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        # Determine the protocol name
        proto_name = "Other"
        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
            
        print(f"\n[+] New Packet Captured:")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        print(f"    Protocol       : {proto_name} ({proto})")
        
        # Display payload summary if available
        if packet.haslayer(TCP) and packet[TCP].payload:
            print(f"    Payload Summary: {bytes(packet[TCP].payload)[:50]}")
        elif packet.haslayer(UDP) and packet[UDP].payload:
            print(f"    Payload Summary: {bytes(packet[UDP].payload)[:50]}")

def main():
    print("--- Starting Basic Network Sniffer ---")
    print("Listening for network traffic... Press Ctrl+C to stop.")
    
    # Sniff packets and send them to the callback function
    # store=0 means we don't keep packets in memory (prevents memory leaks)
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
