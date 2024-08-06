import matplotlib.pyplot as plt


def initialize_plot(ax, graphs, vars):
    ax.cla()
    lines = []
    for graph in graphs:
        t_min = graph.data_range.minimum
        t_max = graph.data_range.maximum
        timestamps = graph.graph_data[:, 0]
        distance_to_home = graph.graph_data[:, 1]
        x_ang = graph.graph_data[:, 2]
        y_ang = graph.graph_data[:, 3]
        RSSI = graph.graph_data[:, 4]

        label = graph.graph_name

        indices = (timestamps >= t_min) & (timestamps <= t_max)

        l_x_ang, = ax.plot(distance_to_home[indices], x_ang[indices], label=f'x_ang {label}', marker='o', markersize=3)
        l_y_ang, = ax.plot(distance_to_home[indices], y_ang[indices], label=f'y_ang {label}', marker='o', markersize=3)
        l_RSSI, = ax.plot(distance_to_home[indices], RSSI[indices], label=f'RSSI {label}', marker='o', markersize=3)

        lines.extend([l_x_ang, l_y_ang, l_RSSI])

    # Устанавливаем видимость линий в соответствии с состоянием чекбоксов
    for i, line in enumerate(lines):
        if vars[i % 3].get():
            line.set_visible(True)
        else:
            line.set_visible(False)

    # Обновляем легенду
    handles, labels = [], []
    for line in lines:
        if line.get_visible():
            handles.append(line)
            labels.append(line.get_label())

    if handles:
        ax.legend(handles, labels)

    ax.relim()
    ax.autoscale_view()
    ax.grid(True)
    ax.figure.canvas.draw_idle()

