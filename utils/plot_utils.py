import numpy as np
from matplotlib import pyplot as plt

from model.graph import graphController
from plot_controller.plot_controller import initialize_plot
from ui.widgets import update_slider_data

import datetime


def update_plot(fig, ax, plot_frame):
    visible_graphs = graphController.get_visible_graphs()
    graphs = [graph for graph in visible_graphs]
    initialize_plot(fig, ax, graphs, plot_frame)


def format_time(t):
    return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')


def update_slider(ax, displayed_graph_list_widget, slider):
    selected_displayed_files_name = displayed_graph_list_widget.get(displayed_graph_list_widget.curselection())
    selected_graph = graphController.get_graph(selected_displayed_files_name)
    graphController.active_graph = selected_graph
    update_slider_data(slider, selected_graph.graph_data)


def update(val, ax, slider, graph):
    if graph:
        print("AAAAAAAAAAAAA = " + graph.graph_name)

        t_min, t_max = val
        timestamps = graph.graph_data[:, 0]
        distance_to_home = graph.graph_data[:, 1]
        x_ang = graph.graph_data[:, 2]
        y_ang = graph.graph_data[:, 3]
        RSSI = graph.graph_data[:, 4]

        indices = (timestamps >= t_min) & (timestamps <= t_max)

        if len(ax.get_lines()):
            lines = ax.get_lines()
            lines[0].set_data(distance_to_home[indices], x_ang[indices])
            lines[1].set_data(distance_to_home[indices], y_ang[indices])
            lines[2].set_data(distance_to_home[indices], RSSI[indices])

        slider.valtext.set_text(format_time(slider.val[0]) + ' - ' + format_time(slider.val[1]))

        ax.relim()
        ax.autoscale_view()
        plt.draw()
