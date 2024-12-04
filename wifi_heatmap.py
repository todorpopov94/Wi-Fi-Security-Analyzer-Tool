import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(rssi_data, grid_size=(10, 10)):
    heatmap = np.zeros(grid_size)
    for (x, y), rssi in rssi_data.items():
        heatmap[x, y] = rssi

    plt.imshow(heatmap, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(label="Signal Strength (dBm)")
    plt.title("Wi-Fi Signal Heatmap")
    plt.show()


if __name__ == "__main__":
    # Example RSSI data (coordinates and signal strength)
    rssi_data = {(2, 3): -50, (4, 5): -60, (6, 7): -70}
    plot_heatmap(rssi_data)
