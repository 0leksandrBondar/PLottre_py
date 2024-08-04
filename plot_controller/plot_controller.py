from matplotlib import pyplot as plt

from ui.widgets import create_plot_toolbar


def initialize_plot(fig, ax, data_list, labels, plot_frame):
    lines = []
    for i, data in enumerate(data_list):
        distance_to_home = data[:, 1]
        x_ang = data[:, 2]
        y_ang = data[:, 3]
        RSSI = data[:, 4]

        l_x_ang, = ax.plot(distance_to_home, x_ang, label=f'x_ang {labels[i]}', marker='o', markersize=3)
        l_y_ang, = ax.plot(distance_to_home, y_ang, label=f'y_ang {labels[i]}', marker='o', markersize=3)
        l_RSSI, = ax.plot(distance_to_home, RSSI, label=f'RSSI {labels[i]}', marker='o', markersize=3)

        lines.extend([l_x_ang, l_y_ang, l_RSSI])

        create_plot_toolbar(plot_frame, fig)

        ax.relim()
        ax.autoscale_view()
        plt.draw()