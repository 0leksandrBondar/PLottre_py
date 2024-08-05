from model.graph import graphController
from plot_controller.plot_controller import initialize_plot
from ui.widgets import update_slider_data


def update_plot(fig, ax, plot_frame):
    visible_graphs = graphController.get_visible_graphs()
    graphs = [graph for graph in visible_graphs]
    initialize_plot(fig, ax, graphs, plot_frame)


def update_slider(displayed_graph_list_widget, slider):
    selected_displayed_files_name = displayed_graph_list_widget.get(displayed_graph_list_widget.curselection())
    temp = graphController.get_graph(selected_displayed_files_name)
    update_slider_data(slider, temp.graph_data)