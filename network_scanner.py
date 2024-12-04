from scapy.all import Dot11, Dot11Beacon, Dot11Elt


def scan_networks(interface="wlan0mon"):
    print("Scanning for Wi-Fi networks...")
    networks = {}

    def packet_handler(packet):
        if packet.hasLayer(Dot11Beacon):
            ssid = packet[Dot11Elt].info.decode("utf-8", errors="ignore")
            bssid = packet[Dot11].addr2
            rssi = packet.dBm_AntSignal if hasattr(packet, "dBm_AntSignal") else "N/A"
            if bssid not in networks:
                networks[bssid] = {"SSID": ssid, "RSSI": rssi}
                print(f"SSID: {ssid}, BSSID: {bssid}, RSSI: {rssi} dBm")

    sniff(iface=interface, prn=packet_handler, timeout=20)
    return networks


if __name__ == "__main__":
    networks = scan_networks()
    print("Networks found:", networks)
