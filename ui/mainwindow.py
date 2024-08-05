from ui.widgets import *
from utils.data_provider import process_load
from utils.plot_utils import *


def init_main_window():
    window = tk.Tk()
    window.title("Plotter")

    plot_frame = create_plot_frame(window)
    bottom_frame = create_bottom_frame(window)
    checkbox_frame = create_check_frame(bottom_frame)
    list_widgets_frame = create_list_widgets_frame(bottom_frame)

    loaded_files_list_widget = create_loaded_files_list_widget(list_widgets_frame)

    load_button = create_load_button(list_widgets_frame)
    load_button.bind('<ButtonRelease-1>', lambda event: process_load(loaded_files_list_widget))

    displayed_graph_list_widget = create_displayed_graph_list_widget(list_widgets_frame)

    fig, ax = create_plot_widget(plot_frame)
    slider = create_empty_slider(ax)

    graphController.on_change(lambda: update_plot(fig, ax, plot_frame))

    loaded_files_list_widget.bind('<<ListboxSelect>>',
                                  lambda event: add_to_displayed_list(loaded_files_list_widget,
                                                                      displayed_graph_list_widget))

    displayed_graph_list_widget.bind('<<ListboxSelect>>', lambda event: update_slider(displayed_graph_list_widget, slider))

    configure_grid_weights(window, plot_frame)

    window.mainloop()
