import pyshark


def sniff_traffic(interface="wlan0"):
    print("Starting packet capture...")
    capture = pyshark.LiveCapture(interface=interface)

    try:
        for packet in capture.sniff_continuously(packet_count=10):
            print(f"Packet: {packet}")
    except KeyboardInterrupt:
        print("Packet sniffing stopped.")


if __name__ == "__main__":
    sniff_traffic()
