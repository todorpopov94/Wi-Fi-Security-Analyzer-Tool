# Wi-Fi-Security-Analyzer-Tool
A Python-based tool for analyzing Wi-Fi networks, including network scanning, packet sniffing, performance analysis, and heatmap generation.

Features
1. Network Scanning: Identify nearby Wi-Fi networks (SSIDs, BSSIDs, RSSI).
2. Packet Sniffing: Capture and analyze real-time network packets.
3. Wi-Fi Performance Analysis: Measure network latency and throughput.
4. Wi-Fi Heatmap: Generate a heatmap of signal strength for efficient troubleshooting.

Prerequisites
1. Hardware:
- A Wi-Fi adapter that supports monitor mode.
- Compatible with Linux, macOS, or Windows (Linux is recommended for full functionality).
  
2. Software Requirements:
- Python 3.9 or later.
- Admin/root privileges for packet sniffing and monitoring.
  
3. Dependencies: Install the required Python libraries:
  pip install scapy pyshark matplotlib requests ping3

4. Optional Tools:
- Install tcpdump for PyShark-based packet sniffing:
  sudo apt-get install tcpdump
- Aircrack-ng for advanced penetration testing (not included in this script).

Installation
1. Clone or download the repository:
   git clone https://github.com/todorpopov94/Wi-Fi-Security-Analyzer-Tool.git
   
   cd wifi-security-analyzer-tool

3. Ensure your Wi-Fi adapter is set to monitor mode (Linux example):
   sudo airmon-ng start wlan0
Replace wlan0 with your Wi-Fi interface name.

Usage
1. Run the tool with administrator/root privileges to access all features:
   sudo python3 wifi_analyzer.py
2. Main Menu
After running the tool, you’ll see the following options:
Wi-Fi Security Analyzer
1. Scan Networks
2. Sniff Traffic
3. Measure Performance
4. Generate Heatmap
5. Exit

Feature Instructions
1. Network Scanning
Select option 1 to scan for nearby Wi-Fi networks.
Output includes:
- SSID: Network Name.
- BSSID: Router MAC Address.
- RSSI: Signal Strength (in dBm).

2. Packet Sniffing
Select option 2 to capture packets in real-time.
The tool will display captured packets for analysis (useful for troubleshooting).

3. Wi-Fi Performance Analysis
Select option 3 to:
- Measure Latency: Pings Google's public DNS server (8.8.8.8).
- Measure Throughput: Downloads a test file to calculate network speed.

4. Generate Heatmap
Select option 4 to generate a heatmap of Wi-Fi signal strength.
Example data is included. To use your own:
- Collect RSSI (signal strength) values for various physical locations.
- Input the values as a dictionary with coordinates:
rssi_data = {(1, 1): -45, (2, 2): -60, (3, 3): -75}

5. Exit
Select 5 to close the tool.

Advanced Setup
Monitor Mode Setup (Linux)

1. Stop the Wi-Fi adapter:
   sudo ifconfig wlan0 down

2. Enable monitor mode:
   sudo airmon-ng start wlan0

3. After scanning/sniffing, revert to managed mode:
   sudo airmon-ng stop wlan0mon
   sudo ifconfig wlan0 up

Examples
1. Example Output for Network Scanning
Scanning for Wi-Fi networks...
SSID: HomeNetwork, BSSID: 00:1A:2B:3C:4D:5E, RSSI: -40 dBm
SSID: CoffeeShop, BSSID: 11:22:33:44:55:66, RSSI: -65 dBm


2. Example Heatmap Visualization
After selecting the heatmap option, you’ll see a graphical representation of Wi-Fi signal strength.

Known Issues
- Packet sniffing may fail if tcpdump or tshark is not installed.
- Requires root/admin privileges for scanning and sniffing.

Future Features
- Penetration Testing: Deauthentication attacks and handshake captures.
- Spectrum Analysis: Interference detection with external hardware.
- Advanced Mapping: GPS integration for large-scale mapping.

Disclaimer
This tool is intended for educational and ethical use only. Unauthorized scanning or sniffing of Wi-Fi networks may violate laws and regulations. Use responsibly.

Feel free to modify or extend the tool as needed. Let me know if you encounter any issues or require further enhancements!
