from network_scanner import scan_networks
from packet_sniffer import sniff_traffic
from wifi_heatmap import plot_heatmap
from wifi_performance import measure_latency, measure_throughput


def main_menu():
    print("Wi-Fi Security Analyzer")
    print("1. Scan Networks")
    print("2. Sniff Traffic")
    print("3. Measure Performance")
    print("4. Generate Heatmap")
    print("5. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        scan_networks()
    elif choice == "2":
        sniff_traffic()
    elif choice == "3":
        measure_latency()
        measure_throughput()
    elif choice == "4":
        # Example heatmap data
        rssi_data = {(1, 1): -45, (2, 2): -60, (3, 3): -75}
        plot_heatmap(rssi_data)
    elif choice == "5":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    while True:
        main_menu()
