from ui.widgets import *
from utils.data_provider import process_load
from utils.plot_utils import *


def init_main_window():
    window = tk.Tk()
    window.title("Plotter")

    plot_frame = create_plot_frame(window)
    configure_grid_weights(window, plot_frame)
    bottom_frame = create_bottom_frame(window)
    checkbox_frame = create_check_frame(bottom_frame)
    list_widgets_frame = create_list_widgets_frame(bottom_frame)
    vars = [tk.BooleanVar(value=True) for _ in range(3)]

    fig, ax = create_plot_widget(plot_frame)
    create_plot_toolbar(plot_frame, fig)
    slider = create_empty_slider(ax)
    load_button = create_load_button(list_widgets_frame)

    create_check_buttons(checkbox_frame, ax, vars)

    loaded_files_list_widget = create_loaded_files_list_widget(list_widgets_frame)
    displayed_graph_list_widget = create_displayed_graph_list_widget(list_widgets_frame)

    load_button.bind('<ButtonRelease-1>', lambda event: process_load(loaded_files_list_widget))

    graphController.on_change(lambda: update_plot(ax, vars))

    slider.on_changed(lambda val: update(val, slider))

    loaded_files_list_widget.bind('<<ListboxSelect>>',
                                  lambda event: add_to_displayed_list(loaded_files_list_widget, displayed_graph_list_widget))

    displayed_graph_list_widget.bind('<<ListboxSelect>>',
                                     lambda event: update_slider(displayed_graph_list_widget, slider))

    window.mainloop()

