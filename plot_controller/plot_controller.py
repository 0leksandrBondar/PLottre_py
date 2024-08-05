from matplotlib import pyplot as plt

from ui.widgets import create_plot_toolbar


def initialize_plot(fig, ax, graphs, plot_frame):
    #plt.cla()

    lines = []
    for graph in graphs:
        distance_to_home = graph.graph_data[:,1]
        x_ang = graph.graph_data[:, 2]
        y_ang = graph.graph_data[:, 3]
        RSSI = graph.graph_data[:, 4]

        label = graph.graph_name

        l_x_ang, = ax.plot(distance_to_home, x_ang, label=f'x_ang {label}', marker='o', markersize=3)
        l_y_ang, = ax.plot(distance_to_home, y_ang, label=f'y_ang {label}', marker='o', markersize=3)
        l_RSSI, = ax.plot(distance_to_home, RSSI, label=f'RSSI {label}', marker='o', markersize=3)

        lines.extend([l_x_ang, l_y_ang, l_RSSI])

    if lines:
        ax.legend()

    create_plot_toolbar(plot_frame, fig)
    ax.relim()
    ax.autoscale_view()
    plt.grid(True)
