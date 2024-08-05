import numpy as np
from matplotlib import pyplot as plt

from model.graph import graphController, DataRange
from plot_controller.plot_controller import initialize_plot
from ui.widgets import update_slider_data

import datetime


def update_plot(fig, ax, plot_frame):
    visible_graphs = graphController.get_visible_graphs()
    graphs = [graph for graph in visible_graphs]
    initialize_plot(fig, ax, graphs, plot_frame)


def format_time(t):
    return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')


def update_slider(displayed_graph_list_widget, slider):
    selected_displayed_files_name = displayed_graph_list_widget.get(displayed_graph_list_widget.curselection())
    graphController.set_active_graph(selected_displayed_files_name)
    update_slider_data(slider)


def update(val):
    t_min, t_max = val
    graphController.set_active_graph_range(DataRange(t_min, t_max))
