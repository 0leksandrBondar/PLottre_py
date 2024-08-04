from ui.widgets import *
from utils.data_provider import process_load, get_dictionary
from plot_controller.plot_controller import initialize_plot


def init_main_window():
    window = tk.Tk()
    window.title("Plotter")

    plot_frame = create_plot_frame(window)
    bottom_frame = create_bottom_frame(window)
    checkbox_frame = create_check_frame(bottom_frame)
    list_widgets_frame = create_list_widgets_frame(bottom_frame)

    fig, ax = create_plot_widget(plot_frame)

    loaded_files_list_widget = create_loaded_files_list_widget(list_widgets_frame)

    load_button = create_load_button(list_widgets_frame, loaded_files_list_widget, plot_frame)
    load_button.bind('<ButtonRelease-1>', lambda event: process_load(loaded_files_list_widget))

    displayed_graph_list_widget = create_displayed_graph_list_widget(list_widgets_frame)

    def foo():
        selected_files = [loaded_files_list_widget.user_data[i] for i in loaded_files_list_widget.curselection()]
        data_list = [get_dictionary(file) for file in selected_files]
        labels = [loaded_files_list_widget.get(i) for i in loaded_files_list_widget.curselection()]
        initialize_plot(fig, ax, data_list, labels, plot_frame)

    graphController.on_change(lambda: foo())

    loaded_files_list_widget.bind(
        '<<ListboxSelect>>',
        lambda event: add_to_displayed_list(loaded_files_list_widget, displayed_graph_list_widget)
    )

    # displayed_graph_list_widget.bind(
    #     '<<ListboxSelect>>',
    #     lambda event: foo()
    # )

    configure_grid_weights(window, plot_frame)

    window.mainloop()
