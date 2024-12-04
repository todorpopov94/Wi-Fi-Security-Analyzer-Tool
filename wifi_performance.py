import time
import requests
from ping3 import ping


def measure_latency(host="8.8.8.8"):
    print(f"Pinging {host}...")
    latency = ping(host)
    if latency:
        print(f"Latency to {host}: {latency * 1000:.2f} ms")
    else:
        print(f"Failed to ping {host}.")
    return latency


def measure_throughput(url="http://speedtest.tele2.net/1MB.zip"):  # Here you can insert an URL by your choice
    print("Measuring download speed...")
    start_time = time.time()
    response = requests.get(url, stream=True)
    total_size = 0
    for chunk in response.iter_content(chunk_size=1024):
        total_size += len(chunk)
    elapsed_time = time.time() - start_time
    throughput = total_size / elapsed_time / (1024 * 1024)  # in Mbps
    print(f"Download speed: {throughput:.2f} Mbps")
    return throughput


if __name__ == "__main__":
    measure_latency()
    measure_throughput()
